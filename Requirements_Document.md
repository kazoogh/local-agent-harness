# Requirements Document

Local Study Assistant | Team: Local Agent Systems | Team member: Jason Galanie

## 1. Version and change log

| Version | Date | Change | Author |
| --- | --- | --- | --- |
| 1.2 review draft | 2026-11-19 | Linked the test plan and updated the companion specification version; requirement statements, IDs and priorities unchanged. | Jason Galanie |
| 1.1 review draft | 2026-11-19 | Added the constraints essay and reconciled CON sources; no requirement IDs or priorities changed. | Jason Galanie |
| 1.0 review draft | 2026-11-19 | First consolidated baseline from User Stories, D0-D2 and Week 8 plan; advisor review pending. | Jason Galanie |

REQ identifiers are new stable IDs. Existing D2 NFR-01 through NFR-09 retain their meanings. A dropped requirement will remain marked withdrawn with a reason/version; no ID is reused or renumbered. Earlier US/AC/FR labels remain source references. These formal priorities and acceptance conditions need my review before approval.

## 2. Purpose and scope

Goal: Help students keep notes and make study materials on their own computer for free. I want students to preserve original course notes, retrieve relevant evidence and review supported practice locally. This document states what is required; [Technical_Specification.md](Technical_Specification.md) v1.2 states how it maps to the existing design.

The first release follows the Week 8 capacity proposal: the existing local web prototype, readable PDF/text sources, semantic retrieval, checked guides/cards, self-rated practice and data control. Native bridging, recurring calendars, PPTX and automatic lecture organization stay outside this release, with retained IDs. Full D2 completion is not promised at 4-8 hours/week; advisor agreement on reduced scope remains open.

## 3. Stakeholders and user goals from Week 4

| Stakeholder / role | Goal and evidence | Source |
| --- | --- | --- |
| Students (primary) | Kevin Chu and Callie Galanie interviews identified the need for practice from course material; retain evidence links and editable drafts. | US-01/02 |
| Me, maintainer (secondary) | Support local study without a hosted-model bill for each session. | US-03 |
| Assistive-technology users (hidden) | Use keyboard and spoken labels independently; direct stakeholder validation is still pending. | US-04 |
| Student taking notes (primary) | Keep extra explanations beside slides and preserve original words. The lecture-helper idea is mine, not an attributed interview finding. | US-05; UC-01 |
| Advisor / peer reviewers | Review scope, feasibility and design. No advisor is assigned; actual D2 peer feedback is still missing. | D2 sec.6; Q1/Q2 |


<!-- pagebreak -->

## 4. Glossary

Terms and roles are defined once here; the specification uses this glossary.

| Term / role | Definition |
| --- | --- |
| Student / primary stakeholder | Student: person capturing material and studying. Primary stakeholder: direct recipient of that study benefit. |
| Maintainer / secondary stakeholder | Maintainer: developer supporting the app. Secondary stakeholder: role enabling delivery rather than receiving its main benefit. |
| Hidden stakeholder | Affected user whose needs can be overlooked; here, a student relying on keyboard or screen-reader access. |
| Advisor / peer reviewer | Advisor: faculty supervisor of scope/design. Peer reviewer: another class team providing attributable design feedback. |
| Course / class session | Course: subject library. Class session: optional dated meeting belonging to one course. |
| Source / original note / revision | Source: identified saved material. Original note: unchanged student capture. Revision: separately saved later version. |
| Passage / source location | Passage: bounded extracted retrieval text. Source location: exact note, PDF page or slide containing it. |
| Evidence / citation | Evidence: supporting source text. Citation: stored passage reference and exact quote span linking an item to that text. |
| Study item / draft / active | Study item: learning content. Draft: awaiting review. Active: accepted and eligible for practice. |
| Guide / flashcard / quiz | Guide: review outline. Flashcard: question/answer recall item. Quiz: practice-question set with feedback. |
| Practice / self-rating / review event | Practice: answer/reveal/source flow. Self-rating: again/good choice. Review event: one saved scheduling update. |
| Ollama / model profile / digest | Ollama: model runtime. Profile: selected model configuration. Digest: artifact identity preventing incompatible model/vector mixing. |
| Embedding / semantic retrieval / RAG | Embedding: numeric text vector. Semantic retrieval: meaning-based passage ranking. RAG: provide retrieved text to generation. |
| Index / library revision | Index: searchable passages/embeddings. Library revision: course change counter checked before result publication. |
| Job / cancellation / retry | Job: saved background task/status. Cancellation: stop publication. Retry: another attempt under the error policy. |
| Local / loopback / managed file | Local: on the student device. Loopback: host-only address. Managed file: app-owned copy, distinct from the original. |
| Import / export / snapshot | Import: selected-file extraction. Export: portable versioned data/files. Snapshot: transactionally consistent view. |
| Desktop interface / bridge / consent | Interface: student-facing screens. Bridge: privileged UI/app calls. Consent: explicit permission for model processing. |
| UUID / UTC / ISO 8601 / epoch seconds | UUID: unique ID string. UTC: reference time zone. ISO 8601: standard date/time format. Epoch seconds: seconds since 1970-01-01 UTC. |
| MoSCoW | Must: minimum release. Should: important/negotiable. Could: optional. Won't: excluded from this release. |
| REQ / NFR / CON / TC | REQ: functional behavior. NFR: measurable quality. CON: inherited restriction. TC: planned verification-case ID. |


<!-- pagebreak -->

## 5. Functional requirements

Priority scopes this release. Won't rows preserve future design scope rather than promise delivery. Verification IDs name the primary cases in [Test_Plan.md](Test_Plan.md); the matrix includes added Must coverage, and none is a passed test. Numeric bounds consolidate D0-D2, not benchmark results.

| ID | Measurable statement | MoSCoW | Source story | Verification |
| --- | --- | --- | --- | --- |
| REQ-01 | The system shall save each 1-100,000-character note to exactly one existing course, reject a meeting from another course, and return the same note after restart. | Must | US-05; D0 I4 | TC-001: Save/restart; reject wrong-course session. |
| REQ-02 | The system shall import text/Markdown and readable PDFs up to 20 MiB, 500 pages and 1,000,000 extracted characters; zero readable text shall return NO_TEXT while retaining separately saved notes. | Should | US-05; AC-01.2 | TC-002: Readable/empty/limit fixtures; inspect saved note. |
| REQ-03 | The system shall reject every unknown/wrong-course citation or quote unequal to its stored passage slice; accepted references shall open the exact note/page or return SOURCE_GONE. | Must | US-01/02/05; AC-01.1 | TC-003: Valid/invalid quote and removed-source cases. |
| REQ-04 | The system shall permit manual supported-card creation and explicit draft acceptance, with zero draft-status items eligible for active practice before acceptance. | Must | US-02; plan T9 | TC-004: Create, accept; inspect active practice. |
| REQ-05 | The system shall request 1-20 local-model flashcard drafts, retain only checked candidates and return NO_SUPPORTED_ITEMS if none survive; failed generation shall leave saved notes unchanged. | Should | US-02/03; D1 B | TC-005: Malformed/unsupported/offline model fixtures. |
| REQ-06 | The system shall search current passages from only the selected course and embedding digest, return at most k=1-32 cosine-ranked matches, break ties by passage ID and reject incompatible vectors. | Must | US-03; D0 search choice | TC-006: Compare exact ranking and course/digest filters. |
| REQ-07 | The system shall generate a source-linked guide from at most 8,000 evidence characters and label uncovered material instead of claiming complete course coverage. | Should | US-01; D1 B | TC-007: Check guide citations, budget and warning. |
| REQ-08 | The system shall return a saved job ID before model inference, expose queued/running/done/failed states, accept cancellation and mark unfinished jobs INTERRUPTED after restart. | Should | US-03/05; D0 background choice | TC-008: Poll, cancel, restart; continue note saving. |
| REQ-09 | The system shall reveal accepted answers/sources before self-rating; again schedules 1 day, good schedules 3 days initially then doubles to a 30-day cap, with one update per review event ID. | Should | US-02; plan T9 | TC-009: Check interval arithmetic and duplicate events. |
| REQ-10 | The system shall save accepted note edits as new immutable revisions, preserve the original and reject stale base revisions rather than overwrite concurrent work. | Should | US-05; AC-01.1 | TC-010: Inspect originals; attempt stale edit. |


<!-- pagebreak -->

### Functional requirements (continued)

| ID | Measurable statement | MoSCoW | Source story | Verification |
| --- | --- | --- | --- | --- |
| REQ-11 | The system shall immediately remove a confirmed source from search/dependent practice, report managed-file cleanup as pending until complete, and leave the student-owned original file unchanged. | Must | US-05; data-control plan | TC-011: Delete and inspect dependents; lock managed file. |
| REQ-12 | The system shall export a consistent course snapshot as versioned JSON and managed files with SHA-256 manifest hashes; denied/full destinations shall fail without modifying course data. | Should | US-05; data-control plan | TC-012: Check manifest/hashes; denied/full destination. |
| REQ-13 | The system shall obtain consent before background model indexing, retain selected profile digests and disable model work on consent revocation or profile mismatch until corrected. | Should | US-03/05; D2 setup | TC-013: Toggle consent; replace digest; check gating. |
| REQ-14 | The system shall display job outcomes without stealing keyboard focus, poll no faster than once per second and coalesce repeated unchanged announcements. | Could | US-04; D0 progress choice | TC-014: Repeat status polls; inspect focus/announcements. |
| REQ-15 | The system shall expand up to 14 meeting rules per course over at most 366 days, preserve referenced sessions and require an explicit decision for ambiguous/nonexistent local times. | Won't | US-05; D0 calendar choice | TC-015: Deferred calendar/DST fixtures when rescheduled. |
| REQ-16 | The system shall keep lecture organization as a separate checked suggestion, accept it as a new revision and create zero slide additions/questions when selected slides have no readable text. | Won't | US-05; UC-01; AC-01.1/2 | TC-016: Deferred accept/stale/zero-text note-slide cases. |
| REQ-17 | The system shall extract supported PPTX text with 1-based slide locations and reject files exceeding D2 parser limits without publishing partial sources. | Won't | US-05; D2 import design | TC-017: Deferred readable/corrupt/oversized slides. |
| REQ-18 | The system shall expose a privileged desktop bridge only to shipped trusted views, reject untrusted navigation/file tokens and never fall back to a public bridge. | Won't | US-03; D1 desktop target | TC-018: Deferred forged-token/untrusted-view cases. |
| REQ-19 | The system shall store formative quiz attempts with expected answers/references, retain accepted evidence when model feedback fails and make zero automatic grade claims. | Could | US-02; D2 practice design | TC-019: Deferred feedback-failure/saved-attempt fixtures. |

Legacy crosswalk: FR-01 -> REQ-01; FR-02 -> REQ-15; FR-03 -> REQ-02/17; FR-04 -> REQ-06; FR-05 -> REQ-03; FR-06 -> REQ-04/10; FR-07 -> REQ-08/14; FR-08 -> REQ-09; FR-09 -> REQ-11/12; FR-10 -> REQ-13/18. Source IDs are preserved rather than reused.


<!-- pagebreak -->

## 6. Non-functional requirements

The IDs retain D2's privacy, cost, accessibility, reliability, access, setup, diagnostics, performance and evaluation meanings. Thresholds operationalize those intentions. Demo PC specifications and actual measurements remain open.

| ID | Measurable statement | MoSCoW | Source story | Verification |
| --- | --- | --- | --- | --- |
| NFR-01 | The system shall make zero cloud-content requests in the local-only workflow, require explicit consent before model processing and log zero note/prompt/answer text in diagnostics. | Must | US-03/05; D2 privacy | TC-020: Inspect calls/logs, consent and local-profile gating. |
| NFR-02 | The system shall require zero paid API keys, subscriptions or hosted app services for capture/local practice and distribute original project code under the repository MIT license. | Must | US-03; D0 cost; LICENSE | TC-021: Run without account/key; inspect license/notices. |
| NFR-03 | The system shall support 100% of the scripted open-course, capture, save, practice, reveal, open-source, return and rate steps with keyboard-only input, visible focus and meaningful spoken labels. | Should | US-04 | TC-022: Execute eight steps with keyboard/screen reader. |
| NFR-04 | The system shall lose zero committed notes across ten fault cases: empty/bad import, model refusal/timeout, stale evidence, cancellation/restart, locked write, failed migration and locked-file deletion. | Must | US-03/05; D2 reliability | TC-023: Run ten cases; compare saved-note hashes. |
| NFR-05 | The system shall bind the release prototype only to loopback, reject all off-allowlist Host/Origin requests and execute zero student/model strings as HTML; no shared-account isolation is claimed. | Must | US-03/05; D0 local boundary | TC-024: Inspect bind; send hostile headers/text. |
| NFR-06 | The system shall complete one documented capture-to-practice run on a clean Windows account with zero source edits; manual Python setup is an allowed packaging fallback. | Should | US-03; D2 setup; plan T14 | TC-025: Follow setup on clean account; record failures. |
| NFR-07 | The system shall keep at most five 1-MiB metadata log files, return logged=false on diagnostic failure and cause zero note-save failures solely from unavailable logging. | Could | US-03/05; D2 reliability | TC-026: Force rotation/denied log output; save note. |
| NFR-08 | The system shall acknowledge all ten sequential 100-character note saves within 1 second each on the nominated Windows demo PC with 5 courses/5,000 passages; model requests shall enforce a 60-second deadline. | Should | US-05/03; D0 timing; D1 size | TC-027: Time ten saves outside import/inference; stall model. |
| NFR-09 | The system shall provide evaluation counts for source support, clarity, usefulness and failures on at least 20 permitted candidate questions, with zero measured learning-gain claims from that sample. | Should | US-01/02; evaluation plan | TC-028: Inspect labeled sample and counts/limitations. |


<!-- pagebreak -->

## 7. MoSCoW summary

### Must

REQ-01, REQ-03, REQ-04, REQ-06, REQ-11, NFR-01, NFR-02, NFR-04, NFR-05.

### Should

REQ-02, REQ-05, REQ-07, REQ-08, REQ-09, REQ-10, REQ-12, REQ-13, NFR-03, NFR-06, NFR-08, NFR-09.

### Could

REQ-14, REQ-19, NFR-07.

### Won't

REQ-15, REQ-16, REQ-17, REQ-18.

9 of 28 requirements are Must (32%). They protect capture, checked evidence, acceptance, retrieval, deletion and the local safety/cost boundary. Should work remains planned but negotiable when a measured schedule risk triggers replanning; planning a task does not make every feature Must.

Won't also includes OCR, LMS integration, cloud sync, automatic grading, audio/video transcription, multi-user hosting and a claimed optimized learning model. Re-entry requires a logged scope/estimate/priority change.

## 8. Inherited constraints

The constraints now trace to [Constraints_Essay.md](Constraints_Essay.md), prepared November 19, 2026 from the current project decisions. CON-01 through CON-05 retain their IDs and meanings; D0, ethics and the plan remain supporting sources.

| ID | Inherited constraint | Source |
| --- | --- | --- |
| CON-01 | No required paid API or hosted backend. | Constraints_Essay: Economic; D0/D1 cost |
| CON-02 | One student/OS account on one device; no multi-user service. | Constraints_Essay: Security; D2 2.9 |
| CON-03 | Windows first; target hardware resources are not measured yet. | Constraints_Essay: Economic/Professional; D0 hardware |
| CON-04 | Use permitted content; retain MIT and upstream/model notices. | Constraints_Essay: Legal; LICENSE/NOTICE |
| CON-05 | Sole member; 4-8 hours/week, with proposed 6-hour average. | Constraints_Essay: Professional; owner availability/plan |


<!-- pagebreak -->

## 9. Assumptions and open questions

Dates below are proposed follow-up targets, not instructor deadlines. I own each action as the sole member.

| ID / assumption or question | Owner | Target date | Required resolution |
| --- | --- | --- | --- |
| Q1: No advisor assigned; no advisor review held. | I | 2026-11-23 | Request assignment through the course process; record the actual review date/discussion/edits when held. |
| Q2: Real D2 peer feedback is missing. | I | 2026-11-23 | Collect teams/comments and my two review issues; apply must-fix actions without claiming participation that has not occurred. |
| Q3: Scope and formal priorities need confirmation. | I | 2026-11-23 | Review requirements/priorities myself; obtain advisor agreement on deferred UC-01 coverage. |
| Q4: Exact remaining course deadlines need confirmation. | I | 2026-11-23 | Confirm revised submission/review dates. The pasted October 30 deadline is past. |
| Q5: Target hardware/model artifacts are unqualified. | I | 2027-01-11 | Record Windows/CPU/RAM/model digests; run locality/readiness/performance checks before making claims. |
| Q6: Accessibility and question quality need validation. | I | 2027-03-30 | Run keyboard/screen-reader checks and permitted-material evaluation; disclose missing stakeholder evidence. |
| Q7: Actual availability may fall to 4 hours/week. | I | Weekly from 2027-01-11 | Compare actuals with the proposed 6-hour plan; agree scope/date changes if lower capacity persists. |

Assumptions: one student controls the OS account; source files are permitted; models can be downloaded initially; saved notes/manual practice remain usable without the model. These do not establish protection against a compromised OS or prove model accuracy.

Sources: [Constraints essay](Constraints_Essay.md), [User Stories](User_Stories.md), [D0](Design_Diagrams/D0_High_Level_Design.md), [D1](Design_Diagrams/D1_Detailed_Design.md), [D2](Design_Diagrams/D2_Detailed_Design.md), [Week 8 plan](Planning/Task_and_Milestone_Plan.md) and [ethics](Ethics_Statement.md). This consolidation claims no new interview, review, submission or benchmark.
