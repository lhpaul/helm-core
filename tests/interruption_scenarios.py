#!/usr/bin/env python3
"""Exercise interruption recovery against disposable local Git repositories.

This is a test fixture, not Helm Core runtime or a live GitHub integration.
"""

import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path


def run(*args, cwd=None, check=True):
    return subprocess.run(args, cwd=cwd, check=check, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def git(repo, *args):
    return run("git", "-C", str(repo), *args).stdout.strip()


def fixture(root):
    remote, work = root / "remote.git", root / "work"
    run("git", "init", "--bare", "--initial-branch=main", str(remote))
    run("git", "clone", str(remote), str(work))
    git(work, "config", "user.name", "Fixture")
    git(work, "config", "user.email", "fixture@example.invalid")
    (work / "example.txt").write_text("base\n")
    git(work, "add", "example.txt")
    git(work, "commit", "-m", "base")
    git(work, "push", "origin", "HEAD:refs/heads/main")
    base = git(work, "rev-parse", "HEAD")
    (work / "example.txt").write_text("updated\n")
    git(work, "commit", "-am", "update")
    return remote, work, base, git(work, "rev-parse", "HEAD")


def remote_head(remote):
    result = run("git", "ls-remote", "--exit-code", str(remote),
                 "refs/heads/main", check=False)
    if result.returncode != 0:
        return None
    lines = result.stdout.splitlines()
    if len(lines) != 1:
        return None
    parts = lines[0].split()
    return parts[0] if len(parts) == 2 and parts[1] == "refs/heads/main" else None


def classify(observed, before, intended):
    if observed == intended:
        return "already_applied"
    if observed == before:
        return "not_observed"
    return "unknown"


def child(mode, work, ready, attempts):
    if mode == "after":
        with attempts.open("a") as log:
            log.write("push\n")
        git(work, "push", "origin", "HEAD:refs/heads/main")
    ready.write_text("ready")
    while True:
        time.sleep(1)


def interrupted_case(root, mode):
    remote, work, base, intended = fixture(root)
    ready, attempts = root / "ready", root / "attempts"
    proc = subprocess.Popen([sys.executable, __file__, "child", mode,
                             str(work), str(ready), str(attempts)])
    try:
        deadline = time.monotonic() + 15
        while not ready.exists():
            if proc.poll() is not None or time.monotonic() > deadline:
                raise RuntimeError("child did not reach interruption point")
            time.sleep(0.05)
        proc.kill()
        proc.wait(timeout=5)
        assert proc.returncode != 0
        observed = remote_head(remote)
        result = classify(observed, base, intended)
        if mode == "after":
            assert result == "already_applied"
            assert attempts.read_text().splitlines() == ["push"]
            # Recovery reports the verified effect; it does not dispatch again.
            assert remote_head(remote) == intended
            assert attempts.read_text().splitlines() == ["push"]
        else:
            assert result == "not_observed"
            assert not attempts.exists()
            # Only after read-back may the already-authorized retry be sent.
            with attempts.open("a") as log:
                log.write("push\n")
            git(work, "push", "origin", "HEAD:refs/heads/main")
            assert remote_head(remote) == intended
            assert attempts.read_text().splitlines() == ["push"]
        print(f"PASS: interrupted {mode} push; read-back={result}; attempts=1")
    finally:
        if proc.poll() is None:
            proc.kill()
            proc.wait(timeout=5)


def main():
    if len(sys.argv) == 6 and sys.argv[1] == "child":
        child(sys.argv[2], Path(sys.argv[3]), Path(sys.argv[4]), Path(sys.argv[5]))
        return
    with tempfile.TemporaryDirectory(prefix="helm-core-recovery-") as tmp:
        root = Path(tmp)
        for mode in ("before", "after"):
            case = root / mode
            case.mkdir()
            interrupted_case(case, mode)
        assert remote_head(root / "absent.git") is None
        assert classify(None, "base", "intended") == "unknown"
        assert classify("different", "base", "intended") == "unknown"
        print("PASS: unavailable or unexpected remote head remains unknown")
        try:
            run(str(root / "missing-reviewer"))
        except FileNotFoundError:
            review = "unavailable"
        else:
            raise AssertionError("missing reviewer unexpectedly ran")
        assert review != "clean"
        print("PASS: missing reviewer is unavailable, not clean")


if __name__ == "__main__":
    main()
