# M2 Helm workspace setup

On 2026-10-30, the owner selected the M2 for Core setup under
[issue #11](https://github.com/lhpaul/helm-core/issues/11). Earlier attempts
had timed out. The configured Tailscale peer still reported offline during this
setup; the node was reached over its local network name after its SSH host keys
matched the existing trusted keys for the configured M2 address. The remote
hostname, account and architecture were inspected before changes.

The M2 user's `Git/DevStack` directory already contained Helm and Helm
Knowledge checkouts. No Helm workspace file was found in the inspected Git and
Documents directories, and the intended Core checkout path did not exist. A
fresh Core checkout was cloned from the public `lhpaul/helm-core` repository on
`develop`, at `839610a89e10415386ab28328a0ae4a6e754f7f5`. Its working tree was
clean when checked. This revision predates the PR that records the setup; it is
not a claim that the node automatically tracks later updates.

A new `DevStack - Helm.code-workspace` was created in the M2 user's
`Git/DevStack` directory using exclusive creation, with relative entries for
`helm`, `helm-knowledge` and `helm-core`. The JSON was parsed and all three
paths resolved to directories on that node. The M2 workspace is intentionally
minimal; it is not an exact copy of another machine's workspace. Existing Helm
and Helm Knowledge checkouts, their branches, Fleet and Grok Bot configuration,
and services were not changed. The workspace file is machine-local, not a file
in this repository.

This confirms a checkout and workspace paths, not that an editor opened the
workspace, that GitHub write/review access works on the M2, or that a Fleet or
Grok Bot Core session is ready. Tailscale and any selected integration need
their own verification. See the earlier
[Fleet and Helm Dev assessment](2026-10-30-fleet-grok-assessment.md) and
[Fleet #158](https://github.com/lhpaul/dev-fleet/issues/158).
