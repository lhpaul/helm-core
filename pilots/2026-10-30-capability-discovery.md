# Pilot: capability discovery work item

This retrospective records the real execution of
[Helm Core issue #3](https://github.com/lhpaul/helm-core/issues/3) against the
[agent work contract](../agent-work-contract.md). The user explicitly requested
that work and authorized merging its PR if the reviewer reported clean. The
work produced [PR #13](https://github.com/lhpaul/helm-core/pull/13). It was
not a separately planned prospective experiment; this record reconstructs the
observable result rather than claiming a new execution took place.

## Outcome and evidence

| Step | Observed result |
| --- | --- |
| Tracker context | Issue #3 specified discovering project instructions, tracker and reviewer capabilities, and honestly reporting unavailable review. Its prerequisite #2, and #2's prerequisite #1, were complete. |
| Change | PR #13 added provider-independent [capability discovery guidance](../capability-discovery.md) and linked it from the contract and README. No runtime or provider adapter was added. |
| Validation | Relative links and diff whitespace were checked. An independent local agent applied the guidance to three simulated observations: missing tracker, explicit permission denial, and pending reviewer. It gave actionable outcomes and did not call any review clean. These were simulated inputs, not live permission failures. |
| Independent review | [Codex GitHub completed review](https://github.com/lhpaul/helm-core/pull/13#issuecomment-6524143638) with no findings for head `03c3cbba17224b6436c80e37cffae553ca3b6a09`. The [review receipt](https://github.com/lhpaul/helm-core/pull/13#issuecomment-6524161002) identifies that revision. GitHub review-thread read-back reported no threads at that head. |
| Merge and tracker | PR #13 merged into `develop` as `18dd10685a79dd3993ad103e886483b48da73ce2`; issue #3 closed and the shared Helm board reported Done. These are merge and tracker evidence, not a release or consumer-adoption claim. |

## Timing and interventions

- GitHub records PR creation at **13:36:08 UTC** and merge at **13:38:06 UTC**
  on 2026-10-30: **1 minute 58 seconds** from PR creation to merge. This excludes
  investigation, drafting and local validation before the PR existed; it is not
  end-to-end task duration.
- The agent requested Codex review at **13:36:15 UTC**. The clean receipt was
  created at **13:37:28 UTC**, about **1 minute 13 seconds** later. This is
  elapsed time between GitHub events, not measured model execution time.
- The user initiated issue #3 and had already authorized merging a clean PR.
  The agent opened the PR, requested the independent review and merged after
  verifying the reviewed head. No additional human decision was needed during
  this observed PR interval. The reviewer reported no findings, so no
  review-driven correction was needed.
- GitHub reported no configured CI checks for the PR. The absence of checks is
  not a passing CI result. A transient GitHub read-back timeout after the merge
  was resolved by a subsequent read; the merge was not repeated.

## What this shows and its limits

The contract and discovery guidance were used on an actual, authorized change
with a tracker item, reviewable diff, independent current-head review, and a
verified merge. The work was limited to documentation in Helm Core itself. It
does not establish a general success rate, live denied-access behavior,
recovery from an interrupted mutation, performance across other repositories,
or that the prototype is ready to replace ADF or Helm. The GitHub event times
above are a small baseline, not a comparison with the older workflows.

The next useful pilots should exercise a different project and tool context,
and the separately tracked interruption and mockup journeys, before drawing
broader conclusions.
