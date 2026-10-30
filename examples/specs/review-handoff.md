# Illustrative spec: review handoff

This example demonstrates how to carry a selected mockup into product
definition. It is not an approved Helm Core product feature or design.

## Outcome

Help a person understand that an independent review is pending and find the
change being reviewed. Product behavior and authorization are not defined by
the mockup alone.

## Selected design reference

- **Mode:** living in-repository source; the linked file is the canonical
  example, not a copied work-item snapshot.
- **Source:** [review-handoff.svg](../mockups/review-handoff.svg), review-pending
  card and its action.
- **Reviewed bytes:** SHA-256
  `99bd18b0843412adb683d625f14d77445eb4823e9e864d4311397129cdc5d57b`.
  This digest identifies the source used for this example; the version in the
  merged repository also has a Git revision. Recheck the reference and revisit
  the spec if the living source changes.
- **Observation:** the selected view shows a pending-review message and an
  “Open the change” action. The reference was rendered and inspected for this
  example.

## Behavior and open questions

- Proposed behavior: show the pending state for the relevant change and provide
  a way to open it. This is a definition example, not evidence of implementation.
- The mockup does not define the destination, unavailable-review behavior,
  authorization, or post-review states. Resolve those with the product owner
  before implementing them.
- Do not infer a clean review from the pending state or from the illustration.

## Handoff

Planning, implementation, and review should inspect the reference and its
recorded version, carry the open questions forward, and verify the implemented
behavior and visual result where applicable. If the reference is unavailable,
report it as blocked rather than guessing the appearance.
