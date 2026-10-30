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
