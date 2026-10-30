# Recover from interruption or unavailable tools

Use this guidance with the [agent work contract](agent-work-contract.md) and the
target project's instructions. It describes how an agent reasons about recovery;
it is not an automated journal or a guarantee that any provider supports a
particular read-back or retry.

## Establish what is known

After a timeout, termination, lost response, or unavailable tool, preserve
local work and identify the target, requested action, intended revision or
effect, and the last reliable evidence. A launched command or acknowledgement
is not proof of completion; an error or lost response is not proof of failure.
If the tool or target is unavailable, report the outcome as unknown and state
what evidence is needed. Do not fabricate a successful review or mutation.

Check whether an earlier process is still running before deciding to retry. If
it might still perform the action, stop and reconcile it using the project's
rules. Do not replay an uncertain remote mutation while the effect is unknown.
Use an independent, authorized read of the exact target and relevant identity;
respect current user authority, revision, project policy and risk limits.

## Choose a continuation

- **Effect verified:** report the evidence and continue with any remaining
  authorized work. Do not repeat the action merely because its response was lost.
- **Expected pre-action state observed:** a retry may be considered only when
  the read-back is sufficient for that operation, the retry is safe and still
  authorized, and relevant prerequisites are rechecked. A current state alone
  does not prove that no prior side effect occurred.
- **Missing, inconsistent, stale or inaccessible evidence:** preserve the
  unknown state, report the blocker and obtain the necessary evidence or human
  decision. An unrelated current revision is not proof of either outcome.

Different operations have different evidence. A Git ref equal to a desired
commit can establish that ref's present value; it does not prove a PR was
merged, a tracker was updated, a notification was delivered, or a deployment
occurred. Check each required outcome independently. A retry that is safe for
a specific Git ref is not automatically safe for an API with additional side
effects.

## Controlled exercise

Run `python3 tests/interruption_scenarios.py` from the repository root. The
fixture creates disposable local Git repositories, interrupts a child process
before a push and after the local remote ref was updated, and reads that ref
before deciding what to do. It also checks unavailable and unexpected read-back
results. It deletes its temporary repositories on normal completion.

The exercise proves only the observed local fixture behavior. It simulates a
lost parent-level result after the child has received Git's success; it does
not interrupt a live GitHub request, prove remote API behavior, or implement an
agent runtime. See the [pilot record](pilots/2026-10-30-interruption-recovery.md)
for the observed run and limitations.
