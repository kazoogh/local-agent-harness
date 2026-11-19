# Test Plan

Local Study Assistant | Local Agent Systems | Team member / QA lead: Jason Galanie

Version 1.0 review draft | November 19, 2026 | Baseline: Requirements_Document.md v1.2 and Technical_Specification.md v1.2. I own all component cases as the sole member. Every execution status is Not Run; this is a spring execution plan, not a results report.

## 1. What is being tested this cycle

In scope: REQ-01-13 for C1 Desktop interface, C2 Course workspace, C3 Material importer, C4 Study engine, C5 Ollama connection, C6 Local data store, C7 access and C9 setup; NFR-01-06/08/09 and CON-01-05 cover local access, data safety, usability, performance and evaluation. The nine Must IDs (REQ-01/03/04/06/11, NFR-01/02/04/05) are the major requirements; each has three cases, including failure/boundary checks. Reliability/provenance run first.

Out of scope: Could REQ-14/19 and NFR-07 (full C8 status, richer C11 feedback, C10 rotation); Won't REQ-15-18 (recurring calendar, C12 lecture organization, PPTX, native bridge). Their seven TC reservations remain deferred, not removed. Current partial status/log guards are still exercised where privacy/access Musts depend on them. OCR, cloud sync, LMS integration, shared accounts and learning-gain claims are excluded. I test SQLite/Ollama/parser integration and failure handling, not their internal engines, model training or third-party general correctness. The current synchronous/text-only prototype is not the finished target.

## 2. Verification and validation strategy

I verify types, bounds, state, source relationships, deadlines and recovery against the specification using isolated fixtures and controlled faults. I validate the study workflow against US-01/02/05 with permitted-material guides/cards and review whether the sources help students check answers. US-04 is validated through the keyboard/spoken-label script and, when recruited, an assistive-technology user. Advisor sign-off and peer execution are separate evidence, not inferred from my tests. Neither has happened.

For model-related checks I fix corpus, prompt and artifact digest, record model options and vary ready/unavailable/invalid output plus CPU/GPU mode where supported. Retrieval scores use a float64 oracle with absolute tolerance 0.00001 and exact tie IDs. I repeat the fixed retrieval queries and generation prompt three times; structural citation checks must reject every unsupported reference. At least 20 candidates receive human support/clarity/usefulness labels; no unsupported accuracy percentage or learning gain is invented. Usability runs three eight-step trials. Raw timings and model output are retained only in the isolated synthetic test evidence folder.

| Layer | Approx. cases | Coverage focus |
| --- | --- | --- |
| Unit | 12 | Bounds, vectors, quote spans, rating arithmetic, log payloads |
| Integration | 14 | Save/import/revision/delete/export, job and write races |
| System | 8 | Locality, access, timing, ten fault scenarios, hardware |
| Acceptance | 5 | Manual fallback, keyboard flow, clean setup, quality labels |
| Inspection | 5 | Licensing, local cost, scope/capacity constraints |


<!-- pagebreak -->

## 3. Measurable success criteria

Targets come from the Week 9 baseline; tolerance/trial details are proposed test methods for my review. Exact integer/error/state comparisons allow no tolerance. Threshold violations fail rather than disappear in an average.

| Metric | Target threshold | Measurement method | Req ID |
| --- | --- | --- | --- |
| M01 Notes/revisions | 1-100000 chars; one course; 0 stale overwrites; original hash unchanged | Boundary/restart/version fixtures; count rows and hashes | REQ-01/10 |
| M02 Imports | <=20 MiB, <=500 pages, <=1M extracted chars; 0 text -> NO_TEXT | Separate below/at/above limit trials; readable/empty/corrupt PDFs | REQ-02 |
| M03 Evidence/acceptance | 100% accepted quotes equal stored slice; 0 wrong-course/unknown refs or unaccepted practice items | Compare spans, IDs, active status; delete evidence trial | REQ-03/04 |
| M04 Generation | Count 1-20; 0 supported -> named error; 0 saved-note mutation | Stub valid/invalid counts/output; compare note hashes | REQ-05 |
| M05 Retrieval | k 1-32; 768 finite unit dimensions; scores within 0.00001; exact tie order | F2 float64 oracle; invalid k/dimension/digest trials | REQ-06 |
| M06 Guides/jobs | <=8000 evidence chars; coverage warning; ID before inference; cancel/restart prevents stale publish | Capture stub request; pause/cancel/restart job | REQ-07/08 |
| M07 Practice | again=1 day; good=3 then double/cap30; 86400 s/day; 1 update/event | Freeze T0; inspect due timestamps and duplicate-event counts | REQ-09 |
| M08 Control/export | 0 deleted source in search/practice; cleanup pending until physical removal; 100% manifest hashes match | Lock/unlock managed copy; verify versioned snapshot/hash list | REQ-11/12 |
| M09 Consent/locality | 0 content calls without consent or to cloud; 0 content payloads in logs | Capture calls, unverified profiles, revocation and marker scan | REQ-13; NFR-01 |
| M10 Cost/access | 0 required paid keys/services; loopback only; 100% hostile header rejection; 0 HTML execution | Offline manual flow, listener/header tests, JS sentinel | NFR-02/05 |
| M11 Reliability | 10/10 fault trials: 0 unintended committed-note loss; rollback/recovery explicit | F01-F10; pre/post logical note SHA-256, not DB-file hashes | NFR-04 |
| M12 Usability | 24/24 scripted actions without mouse/trap; labels meaningful; source-return focus restored | 3 trials x 8 actions; record focus/voice and user feedback separately | NFR-03 |
| M13 Setup | 1 clean Windows account completes flow; 0 source edits | Follow published install or documented manual fallback | NFR-06 |
| M14 Timing | 10/10 N100 save acknowledgments <=1.000 s; model deadline <=60.000 s | perf_counter_ns on F4; deterministic deadline clock; raw timings | NFR-08 |
| M15 Quality | >=20 permitted candidates; support/clarity/usefulness/failure counts; 0 learning-gain claims | Human label sheet with source IDs and disagreement counts | NFR-09 |
| M16 Deferred metrics | Retain <=1 status poll/s, 14 rules/366 days, 0 unreadable-slide claims, PPTX limits, trusted bridge and 0 grade claims | Not gated this cycle; activate reserved cases only after logged scope change | REQ-14-19 |
| M17 Deferred logs | <=5 files x 1 MiB; logged=false on error; 0 log-only save failures | NFR-07 reserved for later cycle; privacy redaction still M09 | NFR-07 |

CON-01/02 are checked by M10; CON-03 by the recorded target profile plus M02/M14; CON-04 by a 100% permission/notice inventory; CON-05 by weekly actuals, 20% task contingency and protected gates in the plan. No metric is a promise of already achieved performance.


<!-- pagebreak -->

## 4. Test cases

Use Testing/README.md prerequisites, F1-F4, the fault catalog and the named target methods; these procedures require their implementation before execution. Missing harness/method/version makes the attempted case Blocked, never Pass. Reset per trial; use synthetic data only. Status starts Not Run.

| ID | Description | Steps | Expected Result | Status |
| --- | --- | --- | --- | --- |
| TC-001 | REQ-01: Save/restart; E21 | 1. Reset F1. 2. save_note(CA,null,"N",NOTE). 3. Close/reopen the store; resolve returned sourceId. | One new CA note; returned text/hash equals NOTE after restart; baseline NA unchanged. | Not Run |
| TC-034 | REQ-01: Upper text bound; E01 | 1. Reset F1. 2. Save N100000 to CA with title "Limit". 3. Reload the saved source. | 100,000 code points retained exactly; one source created. | Not Run |
| TC-035 | REQ-01: Invalid save inputs; E01/E23 | 1. Reset per trial. 2. Submit empty text, N100001, missing course, then CA with session SB. 3. Compare rows to pre-call snapshot. | Empty/oversize -> INVALID_INPUT; absent UUID -> NOT_FOUND; CA/SB -> COURSE_MISMATCH; zero writes. | Not Run |
| TC-003 | REQ-03: Exact evidence; E15 | 1. Reset F1. 2. Validate draft D_OK quoting P1[0:len(NOTE)]. 3. Accept and open reference 0. | Valid draft accepted; exact NOTE location/text opens. | Not Run |
| TC-036 | REQ-03: Broken quote span; E15 | 1. Reset per trial. 2. Validate D_OK with one altered quote character, then endOffset+1. 3. Inspect publication. | Both candidates rejected; zero unsupported drafts published. | Not Run |
| TC-037 | REQ-03: Wrong/gone source; E03/E15/E42 | 1. Reset F1. 2. Cite CB passage in CA draft; attempt publish. 3. Confirm-delete accepted CA item source; resolve the removed item ID. | Wrong-course draft rejected; removed item returns NOT_FOUND; no substituted source. | Not Run |
| TC-004 | REQ-04: Explicit acceptance; E43 | 1. Reset F1. 2. Create supported manual card MC. 3. Accept MC; query active practice. | One accepted card is active; answer/quote match stored source. | Not Run |
| TC-038 | REQ-04: Unaccepted draft; E43 | 1. Reset F1. 2. Create MC but do not accept it. 3. Query active practice; reload app. | Zero draft-status cards in practice before or after reload. | Not Run |
| TC-039 | REQ-04: Unsupported manual card; E15/E43 | 1. Reset per trial. 2. Create MC with a nonexistent source, then quote absent from NOTE. 3. Query saved cards. | Both rejected; zero unsupported active cards or new review states. | Not Run |
| TC-006 | REQ-06: Ranking/course filter; E15/E19 | 1. Seed F2 vectors under D1. 2. search_evidence(CA,D1,Q,k=3). 3. Compare with float64 dot-product oracle and IDs. | P1 then P2 then P3; no CB result; scores within 0.00001. | Not Run |
| TC-040 | REQ-06: Vector/k boundaries; E17/E19 | 1. Reset per trial. 2. Query k=1,32,0,33. 3. Repeat with 767 values, NaN and zero vector. | Valid k returns <=k; invalid k/vector gives INVALID_INPUT; no publication. | Not Run |


<!-- pagebreak -->

### Test cases (continued)

| ID | Description | Steps | Expected Result | Status |
| --- | --- | --- | --- | --- |
| TC-041 | REQ-06: Digest/empty library; E13/E19 | 1. Reset with current profile D1. 2. search_evidence(CA,D2,Q,1). 3. Create empty course CE; submit a flashcard task for CE. | Wrong digest -> MODEL_MISMATCH; empty-course task -> EMPTY_LIBRARY; no mixed vectors. | Not Run |
| TC-011 | REQ-11: Confirmed deletion; E22 | 1. Reset F1 plus managed PDF source. 2. deleteSource with current revision and confirm=true. 3. Inspect search/practice and original PDF hash. | Deleted source absent from search/practice; original PDF unchanged. | Not Run |
| TC-042 | REQ-11: Locked managed copy; E22 | 1. Reset managed PDF source. 2. Hold its managed copy open with exclusive lock; delete source. 3. Unlock and restart recovery. | Cleanup pending reported; source unusable immediately; recovery removes copy after unlock. | Not Run |
| TC-043 | REQ-11: Stale delete/job race; E14/E22 | 1. Reset per trial. 2. Delete with stale revision, then confirm=false. 3. In a fresh run delete while generation is paused before publish. | STALE_LIBRARY then CONFIRM_REQUIRED; zero deletion; raced job cannot publish stale evidence. | Not Run |
| TC-020 | NFR-01: Consent and locality; E20/E34 | 1. Reset; capture network/logs. 2. Save NOTE with consent off; request indexing. 3. Enable verified local stub profile and retry. | Zero cloud-content requests; consent-off blocks model processing; consent-on uses loopback only. | Not Run |
| TC-044 | NFR-01: Unverified remote profile; E20/E35 | 1. Reset F1. 2. Select profile REMOTE (localVerified=false). 3. Request index/generation while recording outbound calls. | LOCAL_POLICY/readiness error; zero content requests sent to remote service. | Not Run |
| TC-045 | NFR-01: Content-free diagnostics; E39/E40 | 1. Put marker SECRET_NOTE in note/prompt/answer. 2. Trigger model/parser failures. 3. Scan every app log for the marker and full payloads. | Zero note, prompt or answer payloads in diagnostic files. | Not Run |
| TC-021 | NFR-02: No paid prerequisites; E36 | 1. Use clean settings with no keys/accounts/subscriptions. 2. Save note, create/accept manual MC and practice. 3. Record setup requirements. | Manual workflow completes; zero required paid keys or hosted app services. | Not Run |
| TC-046 | NFR-02: Model missing fallback; E20/E36 | 1. Reset and stop local model stub/runtime. 2. Request drafting. 3. Save another note and practice MC without signing in. | Model error visible; notes/manual practice work; zero mandatory paid-login/key prompts. | Not Run |
| TC-047 | NFR-02: MIT release evidence; E36 | 1. Inspect release source/bundle inventory. 2. Check original code LICENSE and third-party notices. 3. Repeat checklist on a copy missing LICENSE. | Actual release retains MIT notice; missing-notice copy fails release checklist. | Not Run |
| TC-023 | NFR-04: Ten fault trials; E10/E14/E21-E24 | 1. Reset F1 for each F01-F10. 2. Inject the named fault from Fault_Catalog.json. 3. Restart/recover and compare committed NOTE hashes. | 10/10 trials lose zero unintended committed notes; each named failure recorded. | Not Run |


<!-- pagebreak -->

### Test cases (continued)

| ID | Description | Steps | Expected Result | Status |
| --- | --- | --- | --- | --- |
| TC-048 | NFR-04: Write/migration failure; E21-E24 | 1. Reset F1. 2. Lock writer for >2 seconds; attempt save. 3. Inject migration failure after backup; reopen old data. | Failed write rolls back; old committed notes survive; failed migration never silently resets DB. | Not Run |
| TC-049 | NFR-04: Crash before publication; E14 | 1. Reset F1; pause a job before final commit. 2. Terminate app process. 3. Restart, read note and get_job. | Original NOTE unchanged; unfinished job failed/INTERRUPTED; zero partial active drafts. | Not Run |
| TC-024 | NFR-05: Bind and request guard; E25/E28 | 1. Start isolated app. 2. Inspect listener addresses. 3. GET state with allowed host, hostile Host, then hostile Origin. | Only loopback listener; allowed read succeeds; both hostile requests rejected 403. | Not Run |
| TC-050 | NFR-05: Malformed request boundary; E25/E27 | 1. Reset per trial. 2. POST non-JSON, invalid length, then body >300,000 bytes. 3. Compare DB to baseline. | HTTP 400 for each; zero writes or executed payloads. | Not Run |
| TC-051 | NFR-05: Inert injected text; E27/E47 | 1. Store source and model text containing HTML_JS. 2. Open capture, drafts, practice and source views. 3. Observe JS sentinel. | Payload displayed as text; sentinel stays false in all four views. | Not Run |
| TC-002 | REQ-02: Import and limits; E09-E12 | 1. Import readable.pdf and NOTE text. 2. Test F3 byte/page/character boundaries separately with parser stub. 3. Import empty.pdf/corrupt.pdf. | At-limit validator accepts; above-limit rejects; zero text -> NO_TEXT; saved note remains. | Not Run |
| TC-005 | REQ-05: Draft count/invalid model; E13/E15/E19 | 1. Submit count=1,20,0,21 using stub outputs. 2. Feed malformed/unsupported output. 3. Reload saved NOTE. | 1..20 accepted request count; 0/21 reject; no valid draft -> NO_SUPPORTED_ITEMS; NOTE unchanged. | Not Run |
| TC-007 | REQ-07: Guide evidence budget; E15/E17 | 1. Seed >8,000 source characters. 2. Request guide with capture stub. 3. Inspect source payload, citations and coverage notice. | Evidence <=8,000 characters; every reference valid; omitted material explicitly warned. | Not Run |
| TC-008 | REQ-08: Job lifecycle; E14/E18 | 1. Pause model stub; submit task and read ID/status before releasing it. 2. Cancel queued/running trials. 3. Restart unfinished trial. | Submission precedes inference; valid states only; cancel prevents publication; restart -> INTERRUPTED. | Not Run |
| TC-009 | REQ-09: Ratings and event retry; E41-E44 | 1. Freeze T0; reveal MC. 2. Rate again, good(initial), good(old=20) in reset trials. 3. Resend same eventId/payload. | Intervals 1,3,30 days; due=T0+days*86400; one update for duplicate event. | Not Run |
| TC-010 | REQ-10: Immutable note edit; E22/E46 | 1. Reset F1; updateNote with current base/revision. 2. Read original and new source. 3. Submit another update from stale base. | Original unchanged; one new revision; stale update rejects with no overwrite. | Not Run |


<!-- pagebreak -->

### Test cases (continued)

| ID | Description | Steps | Expected Result | Status |
| --- | --- | --- | --- | --- |
| TC-012 | REQ-12: Export and failure; E24 | 1. Export CA to temp destination. 2. Verify manifest/version and file SHA-256s. 3. Repeat with denied/full destination. | Consistent snapshot/hashes; destination errors explicit; course data unchanged. | Not Run |
| TC-013 | REQ-13: Profile/consent changes; E34/E35 | 1. Start job under verified D1 and consent=true. 2. Revoke consent or replace digest before publish. 3. Request another job. | Old job cannot publish; new model request gated until consent/profile readiness restored. | Not Run |
| TC-022 | NFR-03: Keyboard/spoken script; E04/E29-E32 | 1. Run the eight actions in Usability_Script.md with keyboard/screen reader. 2. Repeat three trials. 3. Record focus and announcements. | 24/24 actions work without mouse/trap; spoken labels meaningful; source return restores focus. | Not Run |
| TC-025 | NFR-06: Clean-account install; E28/E36 | 1. Create clean staging account. 2. Follow release instructions without source edits. 3. Capture/import/create/accept/practice and record dependency failures. | One full run completes with zero source edits; manual Python setup may be documented fallback. | Not Run |
| TC-027 | NFR-08: Save/deadline timing; E17/E21 | 1. Generate F4 (5 courses/5,000 passages). 2. Time ten N100 saves with perf_counter_ns. 3. Advance fake model clock to 60 seconds. | 10/10 acks <=1.000 s; deadline abort by 60.000 s; report raw timings/hardware. | Not Run |
| TC-028 | NFR-09: Labeled quality sample; E15/E47 | 1. Collect >=20 permitted candidate questions with source IDs. 2. Label support, clarity, usefulness and failures. 3. Report counts and reviewer disagreements. | >=20 records/counts; zero unsupported learning-gain claims; provenance reported separately from correctness. | Not Run |
| TC-029 | CON-01: Local cost constraint; E36 | 1. Inventory required runtime services and credential prompts. 2. Execute manual workflow offline except loopback. 3. Inspect documented downloads/costs. | Zero required paid APIs/hosted app services; hardware/download costs disclosed. | Not Run |
| TC-030 | CON-02: Single-user boundary; E25-E28 | 1. Inspect deployment and listener. 2. Attempt off-allowlist request as in TC-024. 3. Inspect account/isolation claims. | Loopback only; request rejected; no public/multi-user isolation claim. | Not Run |
| TC-031 | CON-03: Target hardware record; E09/E17/E36 | 1. Run core flow on DEV-01. 2. Record CPU/RAM/GPU/runtime/browser and model digest. 3. Check bounded input behavior from TC-002/027. | One complete environment manifest and measured limits; zero universal laptop-fit claim. | Not Run |
| TC-032 | CON-04: Permission/notices; E36 | 1. Inspect every fixture/evaluation source permission. 2. Inspect LICENSE/NOTICE and exact bundled dependencies/model terms. 3. Check release contains no course originals. | 100% source inventory has permission/provenance; required notices present; zero bundled unlicensed course files. | Not Run |
| TC-033 | CON-05: Capacity/scope check; Planning R1/R9 | 1. Compare actual notebook hours with plan weekly. 2. Check 20% task buffer and protected gates. 3. Apply 4-hour availability scenario. | Owner/scope recorded; lower-capacity shortfall triggers replan, not an unsupported completion claim. | Not Run |


<!-- pagebreak -->

## 5. Test environment

DEV-01 was inspected on 2026-11-19: Windows 11 Pro 64-bit, version 10.0.26300/build 26300; Ryzen 7 7800X3D; 31.6 GiB reported RAM; RTX 4080 SUPER; Edge 157.0.4341.60; Python 3.13.5; SQLite 3.49.1; Git 2.49.0.windows.1. This is a development profile, not a representative student-laptop performance claim. No sensors or external hardware are part of this project.

| Environment | Data/configuration | Readiness / evidence |
| --- | --- | --- |
| Development | Isolated temp DB/files; F1-F4; fault/model stubs; fixed clock; loopback only | Current PC profile recorded. Target test adapter and future methods are not yet implemented; no product tests executed here. |
| Staging | Clean Windows account; same recorded OS/Edge/Python baseline for comparison; versioned release commit; no existing user settings | Not provisioned. Before run, pin NumPy/pypdf/Ollama versions, model name/digest/dimension and supported CPU/GPU options; record them in run.json. |
| Pilot | Frozen staging build; permitted material; recruit two students, including keyboard/screen-reader perspective if available | Not recruited; advisor/consent requirements unresolved. Record actual users/feedback; do not substitute my test pass for stakeholder validation. |
| Fixtures/network | F1 fixed courses/note/cards; F2 controlled 768-D vectors; F3 limits/readable/empty/corrupt PDFs; F4 5x1000 passages | Generate under a new temp directory with make_fixtures.py. Offline except loopback, normal local runtime, refused runtime and delayed/invalid stub responses are separate trials. |

Before every run record UTC time, app commit, dependency lock, browser/OS build, CPU/RAM/GPU, screen-reader version, model digest/options, fixture hashes and network mode. Screen reader and Ollama/model versions are not verified yet. Real-model cases are Blocked until pinned; unit fixtures do not require downloaded weights. Use stable test aliases; adapters translate target versus legacy wire formats explicitly. Never run destructive fault tests against the student's real database.

## 6. Pass and fail criteria

A case passes only if every numbered action produces its exact expected state/error/output and every linked metric threshold is met. A single wrong course, bad accepted quote, unintended note loss, remote-content request or executed payload fails the case and blocks release. Missing prerequisites are Blocked; unattempted cases remain Not Run. Preserve failing evidence and file a defect with ID, severity and reproduction; do not overwrite it with the rerun.

Cycle verification passes when all 44 active cases pass, all nine Must groups have 3/3 passes, the ten fault trials meet M11, and no critical/high data-integrity/privacy/access defects remain. Deferred reservations do not count as passes or failed scope. Validation remains pending until actual stakeholder findings and required sign-off are recorded; observed barriers or a missing advisor/pilot prevent claiming project-level acceptance. A documented lower-priority deviation needs explicit owner/advisor disposition, not a silent threshold change.


<!-- pagebreak -->

## 7. Milestones, test activities, owner, and evidence

I am QA lead and every component owner. Run cheap deterministic checks before inference/UI work; record actual testing time in the existing T1-T15 notebook and contingency budget. These are the Week 8 dates, not new instructor deadlines.

| Milestone | Test activity / risk-first layer | Owner | Evidence |
| --- | --- | --- | --- |
| I00 Jan 11; I01 Jan 29 | T4/T5 unit/integration: note bounds, ownership, revisions, manual acceptance and source lookup | I | Seed hashes, test output, DB snapshot; TC-001/003/004 and added Must cases |
| I02 Feb 12; I03 Feb 26 | T6-T8 import/model setup/retrieval: limit, refusal, quote and vector failure checks first | I | Parser/stub logs, ranking oracle, profile manifest; TC-002/005/006/013/040/041 |
| I04 Mar 12 alpha | T9-T11 system walkthrough, guide/rating/delete/export; protected Mar 11-12 for blocking fixes | I | Core demo, timing/DB evidence; TC-007/009/010/011/012/042/043 |
| I05 Mar 26 | T12 ten faults, privacy/access, restore/restart; unit + integration during sprint | I | Fault ledger/hash comparisons/network capture; TC-020/023/024/044/045/048-051 |
| I06 Apr 2 beta | T13 keyboard/spoken-label acceptance and user-script review; protected Apr 1-2 | I | 3x8 action records and real feedback when available; TC-022 |
| I07 Apr 16 RC | T14/T15 clean-account, latency, >=20 quality labels, constraints/notices; protected Apr 15-16 | I | run.json, install log, raw timings/labels; TC-021/025/027-033/046/047 |
| I08 Apr 23 handoff | Full active regression and demonstration readiness before final protected Apr 22-23 block | I | 44-case result index, defects/dispositions, requirement matrix and sign-off; no feature work during Apr 24-29 exams |

## 8. Definition of done

Feature checklist: [ ] requirement/design/test IDs linked; [ ] positive and boundary/failure cases pass; [ ] no source loss/cross-course leak; [ ] evidence retained; [ ] code reviewed; [ ] docs/API/errors updated; [ ] actual hours and known limitations recorded. I can self-review implementation, but independent peer/advisor acceptance is recorded separately.

Project checklist: [ ] all 44 active cases and required metrics pass; [ ] zero unresolved critical/high integrity/privacy/access defects; [ ] lower-priority exceptions approved; [ ] clean setup and permitted-data evaluation recorded; [ ] two cases executed by another team with feedback resolved; [ ] stakeholder validation and advisor sign-off recorded; [ ] frozen source/docs/results ready for handoff.

Review status: no advisor is assigned; no two-case peer exchange has occurred (owner confirmed 2026-11-19). TC-001 and TC-037 are prepared in Testing/Peer_Test_Review.md for exchange; no team, date, feedback or approval is invented. The plan's metrics, cases and done criteria need my review under course rules before becoming an approved execution baseline.
