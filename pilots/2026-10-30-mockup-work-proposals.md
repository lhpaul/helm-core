# Pilot: proposals from a living mockup change

This retrospective applies the [proposal guide](../mockup-work-proposals.md)
to an existing historical mockup change in a private product repository. The
source was selected for this pilot from available history, not supplied as a
new product request. The detailed revisions, design and implementation paths,
and existing issue references are retained privately with the operator; they
are not published here. A reviewer without that access cannot independently
reproduce the private inspection from this public record alone.

## Exercise and result

- Compared a real committed design change with its parent revision and
  inspected the target implementation tree at the base and in the current
  checkout. Rendered the before and after entry screen and two new screens;
  other states were not exhaustively rendered.
- The change suggested two functional units with distinct entry points. Multiple
  visual changes within each unit were grouped together. Shared display, API,
  and test surfaces were flagged for coordination rather than assumed to be
  safely parallel.
- Both candidate outcomes already have closed product issues and related
  implementation files. The recommendation was to avoid creating duplicate
  work. Existing files and closed issues do not prove present-day design
  fidelity; a particular remaining gap would need fresh evidence and review.
- No product issues were created, no product code was changed, and no human
  approval of new work was inferred. Product tests, deployment, and all design
  states were not verified.

The guide requires that a future actionable proposal and its design be presented
for human confirmation before creating its resulting tracker items. This pilot
demonstrates a historical grouping and duplicate check; it does not demonstrate
the confirmation and creation of new items, or prove that all private product
implementation matches the design. Coordinate the fuller design-led flow with
[ADF #1667](https://github.com/lhpaul/ai-dev-framework-template/issues/1667).
