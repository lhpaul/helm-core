# Working on Helm Core

Helm Core is an experiment for Helm, not an approved replacement for ADF or the
existing Helm product. Read the relevant issue and the linked strategy before
starting work.

- Follow the user's instructions, repository rules, and the scope and authority
  given for the work. Ask for a decision when requirements or authority are
  unclear; do not equate missing evidence with success.
- Prefer clear instructions and available project tools. Add deterministic code
  when it demonstrably protects a needed guarantee or reduces a measured burden.
- Obtain appropriate independent review and validate changes at the current
  revision. Report unavailable tools, review, tests and unresolved blockers.
- Protect product and UX intent; do not create work from mockup changes without
  the required human confirmation.
- Keep secrets and machine-local credentials out of the repository. Preserve
  user data, unrelated changes, and existing consumers.
- Branch from `develop` using `feature/<issue>-<slug>` for feature work or
  `fix/<issue>-<slug>` for fixes. Make changes through a PR targeting `develop`.
  Use Conventional Commits with an imperative description under 72 characters.
- Core issues belong in this repository and on shared Helm Project #3. Link
  related ADF or Helm work rather than duplicating it.

## Pull request review

- Every PR receives an independent review using an available reviewer. Codex
  GitHub is the starting primary reviewer; Bugbot is an alternative. Another
  suitable tool or reviewer can be used when appropriate.
- Review the change against its intent, risks, and relevant project context.
  The implementer evaluates findings on their merits, fixes material defects,
  and records a concrete disposition for findings not accepted.
- Review evidence must cover the revision being merged. After a push, assess
  what changed and obtain fresh review of material changes; retain evidence
  connecting the reviewed revision and any independently verified safe delta.
- Consider a second independent reviewer for higher-risk changes, such as
  security boundaries, data migrations, interruption recovery, or changes
  affecting many consumers. A second reviewer is not mandatory for every PR.
- An unavailable, failed, or skipped review is not a clean review. Use another
  suitable reviewer if available; otherwise report the missing evidence and
  follow the applicable authority and repository rules.
- Decide whether a finding blocks based on its demonstrated impact, not its
  source. If review cannot converge, report the remaining disagreement and
  evidence instead of repeating fixes indefinitely.
