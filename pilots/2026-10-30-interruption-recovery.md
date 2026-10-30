# Pilot: interruption recovery

The local fixture in [tests/interruption_scenarios.py](../tests/interruption_scenarios.py)
exercises an interrupted operation and read-back against disposable Git
repositories. It does not contact GitHub or alter a product repository.

## Scenarios

1. **Interrupted before the push:** the child is killed before dispatch. A
   fresh read shows the local remote ref at its expected pre-action commit. The
   fixture then performs the already-authorized push once and verifies the ref.
2. **Interrupted after the push:** the child pushes to a local bare repository,
   then is killed before reporting completion to the parent. A fresh read shows
   the intended commit, and the fixture records the effect without sending a
   second push. An attempt log records one dispatch.
3. **Unavailable or unexpected read-back:** an absent local remote produces no
   readable ref; a different observed value is also classified as unknown.
   Neither is reported as success by the fixture's reference classification.
4. **Unavailable reviewer:** attempting to start a nonexistent fixture command
   raises a missing-file error, which the exercise records as unavailable, not
   a clean review. It does not simulate a vendor's response or credentials.

Run the fixture with `python3 tests/interruption_scenarios.py`. Each scenario
must print `PASS`; a failed assertion or command causes a nonzero exit.

## Limits

The local bare repository is a real Git boundary, but it is not a live GitHub
service. The fixture simulates losing the parent's result after the child has
observed a successful push; it does not prove behavior when a network request is
interrupted inside Git or a provider API. Its classification is test code, not
an implemented Helm Core recovery runtime. It does not establish exactly-once
semantics for tracker writes, comments, deployments, or any side effects outside
the observed Git ref. Further live and operation-specific evidence is needed
before making those claims.
