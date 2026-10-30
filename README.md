# Helm Core

Helm Core is an experimental agent-first development foundation for
[Helm](https://github.com/lhpaul/helm). It explores how capable agents can
deliver work using clear outcomes, project context, explicit authority and the
tools available in each project.

The experiment is independent of Helm's current server and does not replace
Helm or the [AI Development Framework](https://github.com/lhpaul/ai-dev-framework-template).
Existing users remain on their current workflows until a migration is evaluated
and approved.

## Starting point

The [agreed strategy](https://github.com/lhpaul/helm-knowledge/blob/main/strategy.md)
and [cross-project roadmap](https://github.com/lhpaul/helm-knowledge/blob/main/operations/agent-first-roadmap.md)
define the purpose, initial work and decision gates. Helm Core issues live in
this repository and appear on the shared
[Helm project board](https://github.com/users/lhpaul/projects/3).

The first milestones are to define the agent contract, discover project
capabilities, deliver a bounded work item to a reviewed PR, and test both
mockup-to-spec references and human-reviewed work proposals from living mockup
changes. Findings should inform Helm's product direction without assuming that
the present implementation must be recreated.

The [first work-item pilot](pilots/2026-10-30-capability-discovery.md) records
the actual capability-discovery change, review, timing, and its limitations.

## Working in this repository

Read [AGENTS.md](AGENTS.md), the [agent work contract](agent-work-contract.md),
and the relevant work item and project context. Use
[capability discovery](capability-discovery.md) to identify the project's tools
and report missing access honestly. For visual product work, use the
[mockup reference guide](mockup-reference.md) to carry the selected design into
the spec and subsequent work.
Changes go through pull requests targeting `develop`. Use Conventional Commits.
Use tests or other checks appropriate to the change and report what was actually
verified. This bootstrap does not yet provide an implementation or runtime.

## License

[Apache License 2.0](LICENSE).
