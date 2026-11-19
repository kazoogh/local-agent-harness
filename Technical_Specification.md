# Technical Specification

Local Study Assistant | Team: Local Agent Systems | Team member: Jason Galanie

## 1. Version and change log

| Version | Date | Change | Author |
| --- | --- | --- | --- |
| 1.0 review draft | 2026-11-19 | First consolidated baseline from User Stories, D0-D2 and Week 8 plan; advisor review pending. | Jason Galanie |

Traceability baseline: [Requirements_Document.md](Requirements_Document.md) v1.0 review draft dated 2026-11-19, with 19 REQ, 9 NFR and 5 CON IDs. Its glossary, priorities and scope govern this proposal. Designed does not mean implemented; the matrix is not acceptance evidence.

Consolidation log: I assigned stable REQ IDs, retained D2 NFR meanings and made existing timing/load intentions testable. I carried forward the Week 8 capacity-driven prototype-first scope, leaving the full calendar/native/lecture design linked but deferred. This documents the change since the D2 draft; no architecture edit is attributed to a peer/advisor review that has not happened.

## 2. Architecture summary

I retain six logical D0 components: Desktop interface, Course workspace, Material importer, Study engine, Ollama connection and Local data store. They share one device. The current Python web prototype listens at 127.0.0.1:8765 with SQLite and optional Ollama at 127.0.0.1:11434. The first release hardens it; the D1/D2 pywebview bridge is a deferred deployment extension (REQ-18), not current server behavior.

The interface sends capture/course/practice actions to the workspace. Import extracts bounded sections with locations; the store commits originals before indexing. The designed engine embeds current course passages, retrieves exact cosine matches, asks the local model for drafts, validates quote spans and publishes only against an unchanged library revision. Students accept drafts before practice, reveal accepted answers/sources and self-rate. Navigation resolves saved IDs rather than model-supplied paths. Model failures remain separate from note saving.

D2 completes consent/setup, access, status, diagnostics, staged-file recovery and job restart/cancellation. The full recurring calendar, PPTX, native bridge and lecture-assistance flows remain outside this release. The proposed 6-hour average remains within my confirmed 4-8-hour availability; advisor assignment and reduced-scope agreement are open.

Linked diagrams (not duplicated): [D0 blocks](Design_Diagrams/D0_Block_Diagram.svg), [capture flow](Design_Diagrams/D0_Capture_Flow.svg), [study flow](Design_Diagrams/D0_Study_Flow.svg), [D1 model](Design_Diagrams/D1_Data_Model.svg), [D2 data extensions](Design_Diagrams/D2_Data_Extensions.svg), [error flow](Design_Diagrams/D2_Import_Error_Flow.svg), [job lifecycle](Design_Diagrams/D2_Job_State_Machine.svg).


<!-- pagebreak -->

## 3. Interfaces and data formats

### 3.1 Every component boundary

D0 I1-I6 are logical calls; I7 is HTTP. The prototype uses same-origin JSON; D1/D2 describe target named calls, not interchangeable implemented endpoints.

| Boundary | Inputs | Outputs / format source | Protocol / errors |
| --- | --- | --- | --- |
| C1 UI / C2 (I1) | Command {kind,payload}; course/session IDs; dirty text | Result<T>, ViewState, SourceView; D2 2.3 | JSON HTTP now; typed target. UIErrorPresenter retains text on failure. |
| C2 workspace / C6 (I4) | createCourse/save_note; selected IDs, bounded strings | Course, NoteRecord, Session[]; D1 sec.5/D2 2.4 | Transactional calls; reject bad ownership/length/version. |
| C3 importer (I2) | requestKey/courseId/sessionId/fileToken; bounded file | ImportBatch {id,state,sourceId,warnings,error}; D2 2.5 | Picker + worker; empty/timeout/unsupported failures publish no partial source. |
| C4 engine (I3/I5) | course/kind/count/topic/requestKey; digest and vector | JobSnapshot or RankedPassage[]; D1 sec.5 | Worker/store calls; BUSY, INDEX_NOT_READY, stale/invalid candidates fail explicitly. |
| C5 adapter (I6/I7) | embed(profileDigest,texts), generate(profileDigest,prompt) | Finite vectors or text; D2 2.7 | Loopback POST; refusal/timeout/invalid output returns named error. |
| C6 store / SQLite/files | Named records, expected revisions, managed IDs | Rows/references/deletion/export result | SQL + file operations; rollback and staged/deleting-file recovery. |
| C7 access guard | Host/Origin + bounded JSON now; trusted context in deferred bridge | Allowed call or ACCESS_DENIED; D2 2.9 | Local allowlist; no public bridge or password service. |
| C8 status | courseId, optional since time, get_job(jobId) | Jobs/dueCount/accessibility status; D2 2.10 | Poll <=1/s; coalesce unchanged states; errors leave capture usable. |
| C9 setup/config | expectedRevision, aiConsent, model digests | Readiness/profiles/issues; D2 2.11 | Local settings/probe; mismatch/unverified locality gates model work. |
| C10 diagnostics | LogRecord: time/code/component/duration; no source text | {logged:boolean}; D2 2.12 | Local rotating log; malformed/denied output never fails a note save. |
| C11 practice | itemId, response/rating, eventId/expectedVersion | Answer/references or dueAt/interval/version | D2 2.13 + store; NOT_DUE, stale source, duplicate conflicts explicit. |
| C12 lecture helper | baseSourceId, same-course slide IDs, requestKey | Suggestion/additions or named error; D2 2.14 | Deferred job; NO_READABLE_SLIDES creates no additions/questions; stale accept rejects. |

C7-C10 are glue, not extra services; C11 is in Course workspace and C12 in Study engine. Ollama is reused external software; C5 owns integration. Exact remaining fields/signatures stay in [D1 sec.5](Design_Diagrams/D1_Detailed_Design.md) and [D2 sec.2](Design_Diagrams/D2_Detailed_Design.md).


<!-- pagebreak -->

### 3.2 Current prototype HTTP API

HTTP/JSON at 127.0.0.1:8765. POST requires application/json and 1-300,000 request bytes. Rejected Host/Origin -> 403; unknown route -> 404; invalid input/missing record on a known POST -> 400 {error:string}; SQLite failure -> 500 {error:string}. This is current server.py behavior, not the D1 envelope.

| HTTP method / endpoint | Inputs / bounds | Success output / specific failure |
| --- | --- | --- |
| GET /api/state | No body | {courses:CourseRow[],sources:SourceRow[],cards:CardRow[],model_available:boolean} |
| POST /api/courses | {name:string 1-80} | CourseRow; duplicate name -> 400 |
| POST /api/sources | {course_id:string or null,title:string 1-120,content:string 1-100000,kind:capture/material} | SourceRow; missing course -> 400 |
| POST /api/cards | {source_id,question,answer,quote}; Q/A 1-300, quote 1-1000 | CardRow; quote outside source or answer outside quote -> 400 |
| POST /api/sources/delete | {source_id:string} | {deleted:true}; missing source -> 400 |
| POST /api/cards/accept | {card_id:string} | {accepted:true}; not a draft -> 400 |
| POST /api/reviews | {card_id:string,rating:again/good} | {due_at:int epoch seconds,interval_days:int}; not due -> 400 |
| POST /api/cards/draft | {source_id:string} | {cards:[{question,answer,quote:string}]}; <=3; missing model/invalid output -> 400 |

Current wire/database rows: IDs are UUID4 hex strings; text is UTF-8; timestamps are integer UTC epoch seconds.

| Schema / format | Fields and relationships |
| --- | --- |
| CourseRow | id:string PK; name:string unique. |
| SourceRow | id:string PK; course_id:string or null FK; title/content:string; kind:capture/material; created_at:int. |
| CardRow | id/source_id:string PK/FK; question/answer/quote:string; status:draft/active; due_at/interval_days/created_at:int. |
| ReviewRow | id/card_id:string PK/FK; rating:again/good; reviewed_at:int. Source deletion cascades to cards/reviews. |

Known gaps: nullable prototype course ownership, mutable source shape and epoch timestamps need migration/adapters to meet the target contract. Browser upload currently accepts only .txt/.md under 200 KB; PDF and D2 extraction bounds are planned. Current drafting uses the first 12,000 characters and a 45-second timeout; the designed adapter deadline is 60 seconds. An available model name in state is configuration, not proof the runtime is ready.


<!-- pagebreak -->

### 3.3 Designed target calls and formats

Target v1 uses UUID strings, UTC ISO 8601 timestamps and Result<T>={ok:true,data:T,error:null} or {ok:false,data:null,error:{code:string,message:string,retryable:boolean}}. Failed writes roll back. These calls are not newly implemented HTTP routes.

| Method / boundary | Input / bounds | Output / representative errors |
| --- | --- | --- |
| save_note / updateNote | courseId; sessionId optional; title 1-120; text 1-100000; base/revision on update | NoteRecord; INVALID_INPUT, COURSE_MISMATCH, STALE_LIBRARY, STORAGE_ERROR |
| importFile / importStatus | UUID requestKey/course/fileToken; optional session; <=20 MiB/500 sections/1M chars | Batch state/sourceId/warnings/error; NO_TEXT, IMPORT_LIMIT, TIMEOUT, PARSE_FAILED |
| submit_task / get_job / cancelJob | course/kind; count 1-20/topic 1-300 optional; requestKey; jobId for status/cancel | JobSnapshot; EMPTY_LIBRARY, BUSY, INDEX_NOT_READY, CANCELLED, INTERRUPTED |
| search_evidence | course/digest; finite unit vector[768]; k 1-32 | matches/libraryRevision; MODEL_MISMATCH, INDEX_NOT_READY, INVALID_INPUT |
| resolve_reference / accept_item | itemId; referenceIndex 0-7 for resolve | SourceView or active item; SOURCE_GONE, NOT_FOUND, INVALID_INPUT |
| reveal / rate | itemId; again/good; eventId and expectedVersion | answer/references or dueAt/interval/version; NOT_DUE, VERSION_CONFLICT, IDEMPOTENCY_CONFLICT |
| deleteSource / exportCourse | sourceId/revision/confirm; or courseId/destination token | Cleanup state or manifest counts; STORAGE_ERROR, ACCESS_DENIED, DISK_FULL |
| saveSettings / probeModels | expectedRevision, aiConsent, optional model digests | Readiness/profiles/issues; VERSION_CONFLICT, MODEL_MISMATCH, LOCAL_POLICY |
| embed / generate (I7) | embed: 1-32 texts of <=1000 chars; generate: prompt <=12000 chars | float32[768][] or text; <=8 MiB response; TIMEOUT, CONTEXT_LIMIT, INVALID_MODEL_OUTPUT |

I7 JSON: /api/embed sends {model,input,truncate:false}; /api/generate sends {model,prompt,stream:false,format:"json"}. Validate vector count/dimension/finiteness and generation done/response. Reject redirects, proxies and unverified remote profiles; a loopback URL alone does not establish local inference. A failed job is retried as a new request/job; polling never republishes drafts.

Exact NoteRecord, JobSnapshot, StudyItem, RankedPassage, SourceView and Reference fields remain in [D1 sec.5](Design_Diagrams/D1_Detailed_Design.md); D2 supplies added/deferred method shapes. Page/slide numbers start at 1; quote offsets count Unicode code points [start,end). Versions use numbered database migrations; breaking field/type/meaning/range changes require v2 plus an explicit adapter.


<!-- pagebreak -->

## 4. Technology stack

I retain D1 choices and the Week 8 prototype-first deployment. Candidate artifacts need pinned versions/digests and target-machine checks; this consolidation introduces no integration or new license audit.

| Layer | Choice | Justification tied to REQ/NFR/CON |
| --- | --- | --- |
| Backend | Python 3.11+; standard library | Current code; reuse dates, workers and sorting for REQ-01/08/09; CON-05. |
| Storage | SQLite/sqlite3 + managed files | Transactions, FKs and revision/index lookup support REQ-01/03/10/11/12 and NFR-04; CON-01/02. |
| Front end/deployment | HTML/CSS/JS; loopback HTTP | Current capture and keyboard flow for REQ-01/04, NFR-03/05/06. pywebview/PyInstaller remain deferred REQ-18 candidates. |
| Models | Ollama; D1 Nomic embedding and Qwen3-4B candidates | Profiles/consent support REQ-05/06/07/13, NFR-01/02. Retain artifact/model notices under CON-04. |
| Retrieval | NumPy blocks; heapq/sorted | Exact cosine/top-k/ties meet REQ-06. Measure NFR-08 before choosing approximate indexing. |
| Extraction | Text decoding; pypdf candidate | Readable PDF locations and bounded failures support REQ-02/03. python-pptx remains outside release under REQ-17. |
| Setup/diagnostics | SQLite settings; Python logging | Readiness/consent/metadata support REQ-13/14, NFR-01/07; no cloud queue or telemetry. |

## 5. Known constraints

| CON ID | Constraint restated | What it forces or rules out |
| --- | --- | --- |
| CON-01 | No required paid API or hosted backend. | Forces local storage/inference and a manual path; rules out required cloud services. |
| CON-02 | One student/OS account on one device; no multi-user service. | Forces loopback/trusted local boundaries; rules out public deployment and account-isolation claims. |
| CON-03 | Windows first; target hardware resources are not measured yet. | Forces bounded imports/prompts/queue and target-PC tests; rules out a universal laptop-fit guarantee. |
| CON-04 | Use permitted content; retain MIT and upstream/model notices. | Forces permission-cleared fixtures and separate notices; rules out bundling unlicensed course material. |
| CON-05 | Sole member; 4-8 hours/week, with proposed 6-hour average. | Forces staged scope, 20% contingency and protected gates; full D2 completion is not promised by April. |

Week 3 provenance is open because the essay was not found. NFR-08 is an inherited design target with an explicit test load, not an actual measurement. Same-OS-user/runtime trust limits remain. Scope, constraints and priorities are those of Requirements_Document.md v1.0, not a claim of advisor approval.


<!-- pagebreak -->

## 6. Traceability matrix

Baseline: Requirements_Document.md v1.0 review draft, 2026-11-19. In progress means related prototype work has a remaining gap; Designed means the named design exists; Planned means scheduled verification/delivery. TC-001-TC-033 reserve stable Week 10 case IDs, not passed tests or renamed existing unit tests.

| Req ID | Description | Design Component (D0/D1/D2) | Status | Test Case |
| --- | --- | --- | --- | --- |
| REQ-01 | Course-bound persistent notes | D1 save_note; D2 C2/C6, 2.8; T4 | In progress | TC-001 (planned) |
| REQ-02 | Bounded readable file import | D2 F2, ImportSupervisor 2.5; C3; T6 | In progress | TC-002 (planned) |
| REQ-03 | Checked evidence and exact source opening | D1 Citation/resolve_reference; D2 C1/C4 | In progress | TC-003 (planned) |
| REQ-04 | Manual cards and explicit acceptance | D1 accept_item; D2 C11, 2.13; T9 | In progress | TC-004 (planned) |
| REQ-05 | Checked local-model flashcard drafts | D1 algorithm B/submit_task; C4/C5; T9 | In progress | TC-005 (planned) |
| REQ-06 | Course-scoped exact semantic retrieval | D1 algorithm A/search_evidence; C4/C6; T8 | Designed | TC-006 (planned) |
| REQ-07 | Evidence-bounded guides and coverage warnings | D1 algorithm B; StudyItem/Citation; C4; T9 | Designed | TC-007 (planned) |
| REQ-08 | Background jobs, cancellation and recovery | D2 F3/JobSupervisor 2.6; C4; T5/T9 | Designed | TC-008 (planned) |
| REQ-09 | Self-rated practice and review intervals | D2 ReviewState/ReviewEvent/rate 2.13; C11 | In progress | TC-009 (planned) |
| REQ-10 | Immutable edits and stale-revision rejection | D1 Source revisions; D2 updateNote 2.8; T4 | Designed | TC-010 (planned) |
| REQ-11 | Source deletion and dependent cleanup | D2 deleteSource/ManagedFileRecovery 2.8; C6; T10 | In progress | TC-011 (planned) |
| REQ-12 | Consistent portable course export | D2 exportCourse 2.8; C6; T10 | Designed | TC-012 (planned) |
| REQ-13 | Model consent and profile readiness | D2 AppSettings/ModelProfile 2.11; C9; T7 | Designed | TC-013 (planned) |
| REQ-14 | Nonintrusive progress announcements | D2 StatusPresenter 2.10; C8 | Designed | TC-014 (deferred) |
| REQ-15 | Recurring calendar (deferred) | D2 F1/ScheduleRule/saveRule 2.4; C2 | Designed | TC-015 (deferred) |
| REQ-16 | Lecture assistance (deferred) | D2 F1/SuggestionEvidence/LectureAssistant 2.14 | Designed | TC-016 (deferred) |
| REQ-17 | PPTX extraction (deferred) | D2 ImportSupervisor 2.5; C3 | Designed | TC-017 (deferred) |
| REQ-18 | Trusted native bridge (deferred) | D2 BridgeGuard 2.9; C1/C7 | Designed | TC-018 (deferred) |
| REQ-19 | Formative quiz attempts (optional) | D2 Attempt/submitAnswer 2.13; C11 | Designed | TC-019 (deferred) |


<!-- pagebreak -->

### Traceability matrix (continued)

| Req ID | Description | Design Component (D0/D1/D2) | Status | Test Case |
| --- | --- | --- | --- | --- |
| NFR-01 | Locality, consent and content-free logs | D2 2.7/2.11/2.12; C5/C9/C10 | In progress | TC-020 (planned) |
| NFR-02 | No required hosted-service cost | D1 local stack sec.6; C6/C9; LICENSE | In progress | TC-021 (planned) |
| NFR-03 | Keyboard and spoken-label workflow | D2 2.3/2.10/2.13; C1/C8/C11; T13 | Designed | TC-022 (planned) |
| NFR-04 | Committed-note fault recovery | D2 F2/F3/2.8; C3/C4/C6; T11/T12 | In progress | TC-023 (planned) |
| NFR-05 | Loopback, request and text boundaries | D0 I1; D2 C7; server.py/web/app.js; T12 | In progress | TC-024 (planned) |
| NFR-06 | Clean-account Windows setup | D2 SetupController 2.11; C9; T14 | Planned | TC-025 (planned) |
| NFR-07 | Bounded diagnostics and graceful failure | D2 DiagnosticSink 2.12; C10; T12 | Designed | TC-026 (deferred) |
| NFR-08 | Save latency and model deadline | D0 timing; D1 size; D2 adapter 2.7; C5/C6 | Planned | TC-027 (planned) |
| NFR-09 | Question-quality evaluation record | D1 algorithm B; evaluation plan; T11/T15 | Planned | TC-028 (planned) |
| CON-01 | No required paid API or hosted backend. | D1 sec.6; C5/C6/C9 | Designed | TC-029 (planned) |
| CON-02 | One student/OS account on one device; no multi-user service. | D0 I1; D2 2.9; C1/C7 | Designed | TC-030 (planned) |
| CON-03 | Windows first; target hardware resources are not measured yet. | D1 size; D2 2.11; C3/C5/C9 | Designed | TC-031 (planned) |
| CON-04 | Use permitted content; retain MIT and upstream/model notices. | D2 2.11; C3/C9; Ethics/NOTICE | Designed | TC-032 (planned) |
| CON-05 | Sole member; 4-8 hours/week, with proposed 6-hour average. | D2 component audit; Planning T1-T15 | Designed | TC-033 (planned) |

Reverse check: all six D0 boxes map to capture/import/retrieval/generation/practice/data-control REQ IDs. C7-C10 map to NFR-01/05/07 and REQ-13/14; C11 to REQ-04/09/19; C12 to REQ-16. Calendar/PPTX/native elements remain linked to REQ-15/17/18 even while deferred. Each CON names a forcing design element. There are zero blank design cells or unresolved design orphans; missing review/essay provenance is recorded as an open evidence issue.

Carry each TC ID into the Week 10 plan with its fixture, steps, expected result and evidence path. Requirements-table verification text supplies initial pass/fail conditions. Deferred cases remain reserved, outside this release acceptance run unless scope changes.


<!-- pagebreak -->

## 7. Record of advisor review

As of November 19, 2026, I have not selected an advisor.

| Record field | Current evidence |
| --- | --- |
| Advisor / actual review date | Not assigned / no review held. |
| Material prepared | Requirements_Document.md v1.0; this specification v1.0; full 33-row matrix; linked D0-D2 and Week 8 plan. |
| Topics actually discussed | None. The proposed agenda below is not meeting evidence. |
| Changes produced by advisor review | None received; no prior edit is attributed to an advisor. |
| Owner / next target | I will request advisor assignment through the course process by proposed target 2026-11-23 and confirm the revised review/submission date. |
| Required lead time | Provide both drafts and matrix at least three days before an agreed future submission deadline. The original October 30 deadline is past; timely prior delivery cannot be claimed. |

### Proposed agenda and change procedure

Confirm reduced scope against D2, the nine Must priorities and 4-8-hour capacity; reconcile Week 3 constraints; inspect each mapping; agree hardware/NFR checks; confirm course dates and real peer-review actions. These are prepared questions, not discussions that have occurred.

After review I will record its actual date, advisor, comments, decisions, affected IDs, file/section edits and version increment. Withdrawn IDs stay in the requirements/change log. Scope or threshold edits must update both documents, the plan and test cases together.

### Evidence and implementation limits

Code inspection covers server.py, store.py, ai.py and web/app.js at baseline e412a98. It identifies current formats/gaps, not measured compliance. D1/D2 contracts remain designed targets. This task adds no runtime code, deployment, test result, peer feedback or advisor approval. The advisor-review criterion is explicitly pending.
