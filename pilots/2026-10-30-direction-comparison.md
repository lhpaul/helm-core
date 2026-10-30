# Core, ADF and Helm: evidence and direction

**Assessment:** 2026-10-30. Recommendation for
[Core #8](https://github.com/lhpaul/helm-core/issues/8), based on the linked
records and local source snapshots. This is a bounded comparison, not a
controlled benchmark, a release decision, or proof of consumer adoption.
The [cross-project roadmap](https://github.com/lhpaul/helm-knowledge/blob/main/operations/agent-first-roadmap.md)
remains the portfolio plan; this record informs its next decision.

## Recommendation: iterate

Continue Helm Core as a small, independent agent-first experiment. Keep ADF
serving existing consumers and prioritize the agreed remote-hub and design
outcomes. Treat Helm as the product and a source of capabilities to evaluate,
not as a runtime dependency of the Core pilot. Integrate a capability only when
a concrete journey shows it is needed and its operational cost is justified.
Do not stop Core or rebuild Helm wholesale on this evidence. No migration or
cutover is approved by this recommendation.

Core's instructions and local exercises make an inexpensive path worth testing,
but they do not yet demonstrate the same operational guarantees or breadth as
the existing systems. ADF's mechanisms protect real workflows and consumers;
Helm has a service, orchestration and review integrations. Remove or replace
none of those guarantees merely because the Core documentation is shorter.

## Observed journeys

| Journey and evidence | Time, intervention and review | Failure and recovery evidence | Limits |
| --- | --- | --- | --- |
| Core: real documentation item [#3 / PR #13](https://github.com/lhpaul/helm-core/pull/13), [pilot](2026-10-30-capability-discovery.md) | PR open to merge 1m 58s; review request to clean receipt 1m 13s. User requested the item and authorized clean merge; agent requested review and merged. Codex GitHub reported no findings on the recorded head. | A transient read-back timeout after merge was resolved by another read, without repeating the merge. Missing access scenarios were simulated. | No configured CI; no measured time before PR creation. One Core documentation change, no product deployment. |
| ADF: delegated-gate fix [#2068 / PR #2079](https://github.com/lhpaul/ai-dev-framework-template/pull/2079) | PR open to merge 30m 43s. The documented invocation explicitly denied delegated merge; the human retained the merge decision. Internal Codex and final external loop reported clean on the recorded head; the PR reports 17 green CI checks, with the template E2E placeholder skipped. | A ready-phase review initially returned `needs_rerun` after evidence changed; a later loop reported clean. The PR reports synthetic red/green regression tests, with GitHub calls mocked. | A workflow bug fix with a different scope, risk and merge authority from Core #3. No task-start timestamp or full human intervention count is established. PR statements and comments describe the run; this is not an independent replay. |
| Helm: repository guidance [PR #114](https://github.com/lhpaul/helm/pull/114) | PR open to merge 23m 41s for an `AGENT.md` change. The PR page exposed no review or issue comments in the inspected fields; this does not prove that no review or other intervention occurred. | No interruption or recovery evidence located in those fields. | Similar artifact category to Core #3, but different request, environment, date and merge authority; task-start time and independent review evidence are unknown. |
| Helm: reviewer integration [PR #116](https://github.com/lhpaul/helm/pull/116) | PR open to merge 22m 06s. The PR records a current-head clean local reviewer and CI success after a branch update; its validation reports 1,753 passing tests. The PR body records a human merge boundary at one stage. | Its described adapter treats missing, stale or malformed review evidence and timeouts as unavailable. Its tests cover timeout and evidence validation. | A feature with much broader scope than Core #3; test and operational assertions are PR-reported, not independently rerun here. The body says no production deployment. |
| Core: design [#5 / PR #15](https://github.com/lhpaul/helm-core/pull/15) and [#6 / PR #16](https://github.com/lhpaul/helm-core/pull/16) | A spec example identifies its visual reference; a historical private product diff yielded two proposed units that already had issues. No new product items were created. | [Proposal pilot](2026-10-30-mockup-work-proposals.md) records incomplete design coverage and inaccessible private details; no new work was confirmed or created. | The example is illustrative, not an approved product spec. The historical pilot is not an end-to-end prospective design-to-tracker journey. ADF's [#1667](https://github.com/lhpaul/ai-dev-framework-template/issues/1667) describes the outstanding design-led flow; its issue text is a desired invariant, not evidence it is delivered. |
| Core: [interruption exercise](2026-10-30-interruption-recovery.md) / [PR #17](https://github.com/lhpaul/helm-core/pull/17) | Independent review was clean; the exercise read the target before deciding whether to continue. | Disposable local Git remotes demonstrate interruption before push and after push success before parent acknowledgement; missing reviewer and unavailable or unexpected read-back are exercised. | Not a live GitHub API interruption, a recovery runtime, or proof of exactly-once effects. ADF's [Protocol 94](https://github.com/lhpaul/ai-dev-framework-template/blob/b1fa591da9ce4dde72a089b85abdf1989eb88907/docs/workflow/development-workflow/protocols/94-batch-merge-protocol.md) describes durable session admission and recovery; that is a documented mechanism, not a comparable measured run. |

The durations are GitHub event intervals, not agent execution time or total
work time. These samples differ in scope, risk, policy and human authority;
they do not show that any approach is faster or safer. A clean review in one
sample is not a defect rate. Missing data is unknown, not zero. The private
mockup record cannot be independently reproduced from its public description.

## Maintainability and portability

- Core currently consists of human-readable guidance plus an isolated test
  fixture; its contract discovers available tools instead of prescribing a
  provider. That reduces the initial surface, but portability to another
  tracker, reviewer or product repository is a hypothesis until exercised.
- In the local ADF source snapshot `b1fa591da9ce4dde72a089b85abdf1989eb88907`,
  `rg --files scripts` listed 451 files and `rg --files docs/workflow` 75.
  These are rough file counts, not lines of code, maintenance cost, production
  usage or a quality score. Some encode recovery, consumer compatibility and
  authority controls that the Core prototype has not replaced.
- In the local Helm source snapshot `1e66895052481d2a3110a2b9b6ed4d9ffe0a2615`,
  the repository contains a web app, API, orchestration packages, tracker and
  review services, and tests. [PR #116](https://github.com/lhpaul/helm/pull/116)
  illustrates both a useful exact-head review boundary and a provider-specific
  adapter plus an installed ADF companion dependency. Source presence does not
  establish current deployments, use, operating cost or portability.
- The existing [Helm strategy](https://github.com/lhpaul/helm-knowledge/blob/5cf8426b92a94f7d1f0e05b33d76884b1b1a42f0/strategy.md)
  describes formal stages and gates. Reconcile that product direction with the
  agent-first roadmap through an explicit reviewed decision before changing it.

## Bounded next steps and decision gate

1. **ADF:** continue [remote hub #1719](https://github.com/lhpaul/ai-dev-framework-template/issues/1719)
   and [design-led #1667](https://github.com/lhpaul/ai-dev-framework-template/issues/1667)
   for current projects. Verify current children and run the intended journeys;
   track release and consumer adoption separately. Owners: ADF maintainers and
   product/design owner for the mockup decision.
2. **Core:** run one prospective, bounded work-to-reviewed-PR pilot in an
   explicitly selected product or disposable repository, with a real available
   tracker and reviewer. Capture start, PR-ready and merge timestamps; human
   decisions and waiting; findings and disposition; failures and recovery;
   tool and permission constraints; and tests. Keep UX confirmation before
   creating proposed design work. Owner: Core maintainers, with product owner
   choosing and confirming the design where applicable.
3. **Helm:** inventory actual deployment, consumers and current review/runtime
   configuration. Use [Core #9](https://github.com/lhpaul/helm-core/issues/9)
   for the Fleet and Grok Bot integration assessment and per-node evidence;
   do not change live services as part of this comparison. Owner: Helm/Fleet
   maintainers and node operators.
4. **Compare again:** choose one similar low-risk journey for each applicable
   path, with comparable scope, authority, review and validation, and record
   the same events from task selection. Include a real authorized interrupted
   or unavailable operation only where its side effects can be independently
   reconciled; otherwise record the gap. One example per path is exploratory,
   not a statistically meaningful benchmark. Owner: portfolio maintainer.

At the next reviewed portfolio decision, **integrate** a specific capability
only if the representative journey meets the needed authority, current-revision
review, recovery and consumer compatibility requirements with an identified
owner and operational cost. **Iterate** if evidence or coverage remains
insufficient but the pilot is useful. **Stop** the experiment if a bounded
pilot shows no worthwhile improvement after accounting for reliability and
maintenance. These are decision criteria, not outcomes already achieved.

Before any consumer migration: inventory each supported workflow and version,
map its existing guarantees and configuration to verified replacements, test
review, failure and recovery on the actual providers and nodes, plan rollout
and rollback, assign an owner, and obtain the applicable product and operator
authority. Keep existing consumers on their current path until that decision.
