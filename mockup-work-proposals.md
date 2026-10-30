# Propose implementation work from a living mockup change

Use this guide when a user asks to turn a design change into implementation
work. Apply the [mockup reference guide](mockup-reference.md), the
[agent work contract](agent-work-contract.md), and the target project's rules.
The agent proposes a breakdown; **a human must confirm it before any resulting
tracker items are created**. This guide does not grant permission to change the
design, implementation, tracker, or other repositories.

## Understand the change and implementation

Identify the canonical living source, the base and proposed revisions, the
screens or states in scope, and the target product and implementation tree.
Inspect the actual diff and render the relevant before and after states. If a
required revision, source, rendering capability, or implementation mapping is
unavailable or ambiguous, report the specific gap and ask for a decision; do
not invent a design or silently assume where it belongs.

Read enough of the implementation, existing work items and project context to
identify the affected units and avoid proposing work already completed or
tracked. A file match alone does not establish behavior or ownership. Record
the compared revisions, relevant paths and observations, while respecting the
source repository's privacy and access restrictions.

## Prepare a proposal

Group changes by **unit of implementation**, not by visual difference. For
example, two visual changes in one component generally form one candidate item;
distinct components may justify separate items if their responsibilities and
dependencies can be separated. Flag shared files, cross-cutting work and
uncertain mappings for the implementation owner instead of promising parallel
work will be conflict-free.

For each proposed item, show:

- The outcome and observable acceptance conditions, including important
  behavior not conveyed by the mockup and any accessibility considerations.
- The design evidence, proposed implementation unit and relevant paths, with
  uncertainty where a mapping is not established.
- Dependencies, overlap with existing work, and a validation approach.
- Open product or design decisions that require a human rather than inference.

Distinguish confirmed observations from assumptions. If no implementation work
is needed, explain the evidence and any remaining uncertainty instead of
inventing an item. A visual diff is not proof that a product has implemented
the design; validate behavior and fidelity when implementation is undertaken.

## Review and handoff

Present the design change and the proposed breakdown together for human review.
Do not create tracker issues or perform other external writes merely to test
the proposal. After explicit confirmation, follow the target project's tracker,
repository, and authority rules; if the design or breakdown changes materially,
review the revised proposal before creating the affected work.

When using an epic's integration branch, follow its actual branch ownership and
graduation rules. Link the approved design reference and work items so the
implementation can travel with the design. The branch arrangement alone does
not prove that the implementation matches the mockup.

The [retrospective pilot](pilots/2026-10-30-mockup-work-proposals.md) records
the boundaries of an exercise on a real design change in a private product.
