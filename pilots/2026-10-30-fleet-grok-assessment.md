# Fleet and Helm Dev integration assessment

**Assessed:** 2026-10-30 for [Core #9](https://github.com/lhpaul/helm-core/issues/9).
This is a read-only assessment, not an enabled integration or a successful
remote execution. Node state and repository revisions are observations at the
assessment time; recheck them before use.

## Decision

Continue Core directly with an authorized agent session for now. Do not
register Core as an `adf` or `helm` Fleet project merely to satisfy the current
schema, and do not expand the Grok Bot Helm Dev agent's scope yet. Neither
integration is a prerequisite to the standalone pilot. Once an actual Fleet or
Grok Bot Core run is selected, choose the smallest safe approach and validate
it on the selected node before relying on it. This assessment does not grant a
new agent permission to start items or merge.

## Fleet

At [Fleet develop `7abae43`](https://github.com/lhpaul/dev-fleet/tree/7abae43bbd605be013f21a9ca700cf39dd66f54a),
[node configuration](https://github.com/lhpaul/dev-fleet/blob/7abae43bbd605be013f21a9ca700cf39dd66f54a/packages/fleet/src/node/config/schema.ts)
and [API contracts](https://github.com/lhpaul/dev-fleet/blob/7abae43bbd605be013f21a9ca700cf39dd66f54a/packages/fleet/src/shared/contracts.ts)
accept motors `adf` and `helm`; the
[database constraint](https://github.com/lhpaul/dev-fleet/blob/7abae43bbd605be013f21a9ca700cf39dd66f54a/packages/fleet/src/server/db/migrations/0007_account_scoped_project_ids.sql)
also encodes those choices. The [readiness check](https://github.com/lhpaul/dev-fleet/blob/7abae43bbd605be013f21a9ca700cf39dd66f54a/packages/fleet/src/node/readiness/index.ts)
requires an ADF marker for `adf` but treats the Helm motor marker as present
without checking for one. Passing that marker check therefore does not establish
Core compatibility. The [start prompt](https://github.com/lhpaul/dev-fleet/blob/7abae43bbd605be013f21a9ca700cf39dd66f54a/packages/fleet/src/node/tmux/start-prompt.ts)
contains a generic notification convention and operator instruction; this alone
does not prove that all dispatch, readiness, access and completion paths are
motor-neutral.

Node configuration declares a project path, motor, agents, permission mode,
allowed directories and optional environment files. Actual configuration is
machine-local and must not be committed. There is no evidence from this
inspection that a running Fleet daemon supports Core. The M6 runtime source
package identifies itself as version `0.2.0`, but the exact running daemon
revision and service health were not verified. The M6 Fleet source checkout was
at `6ba63dc`, older than the inspected remote develop revision. Existing Fleet
[issue #143](https://github.com/lhpaul/dev-fleet/issues/143) reports an M6
update/restart problem; its existence does not prove that today's daemon is
unavailable.

**Owning follow-up:** [Fleet #158](https://github.com/lhpaul/dev-fleet/issues/158)
asks Fleet maintainers to assess existing modes against a small provider-neutral
option, including schema and data migration implications. It does not authorize
configuration or deployment. A new motor name is not a substitute for a
validated runtime path.

## Grok Bot and Helm Dev

The inspected Helm Dev brief in the owner's private knowledge repository
covers `lhpaul/helm` and `lhpaul/helm-knowledge`, not Core. It requires
confirmation for each item, isolated agent checkouts, and excludes the checkout
serving Helm AF and its services. Its Helm-specific board query identifies items
only by number and its issue helper belongs to Helm; neither is sufficient to
route same-numbered issues across Helm and Core safely. The shared workspace
includes additional repos, including the service checkout, and the brief
explicitly avoids using it for these agent sessions. Adding Core to that
workspace does not extend the agent's scope or create an isolated checkout.

The local and M6 brief copies differed in content hash, though both inspected
copies contain the Helm-only scope and old reviewer instructions. Their actual
runtime source and distribution mechanism were not verified. Both describe
CodeRabbit and a pending Helm PR #115, while [#115](https://github.com/lhpaul/helm/pull/115)
and [#116](https://github.com/lhpaul/helm/pull/116) are merged and current
[Helm `AGENT.md`](https://github.com/lhpaul/helm/blob/develop/AGENT.md)
requires local AI reviewer evidence at the current head and says CodeRabbit
auto-review is disabled. This is a brief drift, not proof of a particular live
agent action or an authorization to change its policy.

**Owning follow-up:** [private knowledge issue #12](https://github.com/lhpaul/lh-cerebro/issues/12)
tracks reconciling the authoritative brief and its distributed copy with the
current Helm policy. It preserves item-by-item confirmation and isolation.
If the owner later selects Core coverage, assess extending Helm Dev versus a
separately scoped agent; require repository-qualified issue identity, an
isolated Core checkout and explicit authority. Apply Core's own review rules
and verify its board updates; do not assume Helm's helper or stage writeback
supports Core.

## Node observations

| Node | Observed | Remaining gap |
| --- | --- | --- |
| MacBook | Local Helm workspace contains a Core entry pointing to an existing checkout. The local Fleet config has no Core project. | Workspace was inspected as a file, not opened in an editor. No Fleet Core run or capability validation. |
| M6 | SSH worked; its Helm workspace Core entry resolves to a checkout. The Fleet config has no Core project; the Helm Dev isolated checkout directory had Helm and Helm Knowledge, but no Core checkout. The ordinary Core checkout was at `823cc07` when checked. | The shared workspace is not safe as Helm Dev's agent workspace under the existing brief. No Core agent session, editor open, running Fleet version or service validation. |
| M2 | SSH timed out during this assessment. | A later [workspace setup record](2026-10-30-m2-workspace.md) documents local-network access and checkout setup. Fleet configuration and runtime readiness remain unverified. |

## Before an integration is used

For each selected node, confirm identity and reachable service/version; inspect
its own workspace and configuration without exposing credentials. Establish an
isolated checkout and only the required allowed directories, agent and access.
Verify the authoritative agent brief and applicable per-item/merge authority.
Then exercise an explicitly authorized, bounded Core item through the selected
runtime: confirm correct repository and board identity, prompt delivery,
current-head independent review, safe interruption/read-back and honest final
status. Verify tracker and PR results independently. Record actual behavior,
missing tools and failures, with no inferred production adoption. If a node is
unavailable, leave its setup pending; do not use a different node's result as
proof. Any code or configuration changes belong in the owning repository or
node's proper source of truth and follow its review and deployment rules.
