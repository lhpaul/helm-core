# Carry a mockup into product definition

Use a selected mockup as product context when it is relevant to the work. Follow
the [agent work contract](agent-work-contract.md), the user's direction, and
the target project's rules. A mockup is a visual reference, not an automatic
approval of product behavior or an instruction to create tracker items.

## Select and inspect the reference

Identify the selected source, the screens or states in scope, and the product
question it answers. Read or render the actual reference with an appropriate
tool; a filename, URL, or successful text lookup alone does not establish the
visual content. Ask for the missing choice when multiple sources conflict or
the intended reference is unclear.

If a required source cannot be accessed or rendered, report the reference and
the missing access or rendering capability, preserve the work, and block claims
of design fidelity. Do not substitute an imagined design or claim the reference
was reviewed. Continue independent work where useful. Avoid copying private
design assets or sensitive details into a public repository without authority.

## Reference it in the spec

Record enough context for another person or agent to retrieve and review the
same design:

- The source location, relevant screen/state, and whether it is a **snapshot**
  or a **living source**. Follow the project's link and access conventions.
- An immutable reference where available: a repository commit and path, a
  versioned design artifact, or a content digest for the exact snapshot. For
  mutable sources, record the reviewed revision or retrieval time and any
  limitations. A digest identifies bytes; it does not grant access.
- The intended UX outcome, behavior the mockup does not specify, and relevant
  assumptions or open product decisions. Link to the selected design from the
  spec so implementation and review can find it.

A **snapshot** is a fixed artifact for the work item. Preserve its identity;
do not silently replace it if the source changes. A **living source** is the
canonical design maintained over time. Reference it in place rather than
silently copying it into a stale artifact. Record the version that informed
the spec and revisit the spec if the canonical design changes. If it is part of
an unmerged change, a recorded commit or content digest can identify the
reviewed bytes until a durable repository revision is available.

Carry the reference and any unresolved questions into planning, implementation,
and review. Report what was actually inspected and tested. A referenced design
does not prove the implementation matches it; validate relevant behavior and
visual fidelity using the tools and scope appropriate to the project.

## Example

The [illustrative spec](examples/specs/review-handoff.md) refers to an actual
repository mockup. It demonstrates a living source and its reviewed digest;
the screen is a sample for this work, not an approved product design. A
snapshot can use the same fields with a fixed attachment or versioned file
instead. For design-led work, use the
[mockup work proposal guide](mockup-work-proposals.md); any item creation still
requires the agreed human confirmation.
