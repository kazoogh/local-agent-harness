# Two-case peer execution review

Status: no exchange held; confirmed by the project member on November 19, 2026. Reviewing team, review date, attempted status and feedback are not recorded. This is preparation, not participation evidence.

Share Test_Plan.md, Testing/README.md and the fixture generator with the reviewing team. If target methods/harness are absent, record Blocked and the missing prerequisite; do not claim a successful execution or ask a reviewer to guess an endpoint.

## Case 1: TC-001 / REQ-01

1. Reset F1 using the isolated test store.
2. Call save_note(CA, null, "N", NOTE) through the target adapter.
3. Close/reopen the store and resolve the returned source ID.

Expected: one new CA note, with identical NOTE text/hash after restart, while the original seeded NA remains unchanged. Initial status: Not Run.

## Case 2: TC-037 / REQ-03

1. Reset F1 and attempt to publish a CA draft citing CB's passage PB.
2. Confirm it is rejected and no unsupported CA draft is published.
3. In a fresh supported trial accept the CA item, delete its evidence source and open the old reference.

Expected: wrong-course rejection; confirmed deletion removes the dependent item, so resolving that absent item ID returns NOT_FOUND, with no substituted source. Initial status: Not Run.

## Record after the exchange

Team/name: Pending. Date: Pending. Case IDs: TC-001 and TC-037. Reviewer result/evidence: Pending. Ambiguous steps and requested edits: Pending. Owner: Jason Galanie. Resolution and affected plan version: Pending. Preserve the actual comments and retest result rather than filling this record with assumed feedback.
