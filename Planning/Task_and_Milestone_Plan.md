# Task Lists, Milestones, Timeline, and Effort Matrix

Assignments 5 and 6 | Local Study Assistant | Team: Local Agent Systems | Team member: Jason Galanie

Planning basis: November 18, 2026. I have 4-8 hours a week available for implementation. The proposed spring schedule uses a 6-hour average, never more than 8 hours in a week, with 20% contingency on every task and separate protected milestone blocks. Estimates, risk judgments, and scope priorities below are planning proposals for my review; I have not supplied or approved the individual O/M/P estimates yet.

The pasted deadline is October 28; I do not backdate this plan or claim that missing work was submitted on time. The syllabus gives the Week 1-14 deliverables but only one explicit dated schedule row. Its term label also conflicts with its Fall 2026 cover. I use the supplied assignment dates, the November 25 presentation schedule, repository artifact dates, and UC's 2026-27 academic calendar; unknown course deadlines stay explicitly unconfirmed.

## 1. Task List (Assignment 5)

I use 15 tasks because the rubric requires 10-25 even for my one-member team. The suggested five tasks per member cannot override that minimum. Each task is a bounded part-time work package, normally around one workweek and never more than two calendar weeks. Hours are hands-on effort rather than full-time elapsed duration. The same statements and owner appear in Tasklist.md, Table 1, Table 2 and the work breakdown structure.

T1. Specify release priorities and the requirements/test baseline for Course workspace, Local data store, Study engine, and deferred D2 components. Owner: Jason Galanie.

T2. Document Desktop interface and Course workspace walkthroughs for the scheduled fall presentation. Owner: Jason Galanie.

T3. Document the Course workspace and Study engine design, notebook, and implementation handoff in the Week 14 report. Owner: Jason Galanie.

T4. Develop Local data store migrations, source ownership, immutable note revisions, and citation lookups for the core study flow. Owner: Jason Galanie.

T5. Develop Desktop interface and Course workspace capture, course selection, job status, and source navigation in the existing local prototype. Owner: Jason Galanie.

T6. Develop Material importer handling for text, Markdown, and readable PDFs with bounded extraction and page references. Owner: Jason Galanie.

T7. Develop Configuration/setup and Ollama connection checks for consent, installed local models, timeouts, and typed errors. Owner: Jason Galanie.

T8. Develop Study engine passage embeddings and exact course-scoped semantic retrieval against a bounded fixture library. Owner: Jason Galanie.

T9. Develop Study engine generation and Practice/review for checked study guides, flashcards, answer reveal, and self-rating. Owner: Jason Galanie.

T10. Develop Local data store source deletion and portable export with dependent-item cleanup and recovery checks. Owner: Jason Galanie.

T11. Test Material importer, Study engine, and Local data store for integrated capture, retrieval, draft provenance, practice, and deletion flows. Owner: Jason Galanie.

T12. Test Access boundary, Logging, and Local data store for privacy, request validation, restart, and failure recovery. Owner: Jason Galanie.

T13. Validate Desktop interface and Practice/review keyboard access, spoken labels, status announcements, and source-return focus. Owner: Jason Galanie.

T14. Validate Configuration/setup and Desktop interface installation on a clean Windows account with a documented manual setup fallback. Owner: Jason Galanie.

T15. Document Study engine evaluation, Local data store limitations, release instructions, and the final demonstration evidence. Owner: Jason Galanie.

### Release scope and feasibility

The full D2 design exceeds what I can credibly promise at 4-8 hours a week. This is a proposed staged implementation plan, not a silent change to D0-D2. I must confirm the narrower first release with my advisor before I00. The existing local Python/SQLite web prototype is the baseline. I retain saved originals, readable sources, course-scoped semantic retrieval, checked guides/cards, self-rated practice, evidence links, deletion/export and local-model failure handling.

| D2 area | Planned first-release treatment | Disposition / approval |
| --- | --- | --- |
| Desktop interface / Access boundary | Harden the current loopback interface and source-return workflow; test host/origin/request constraints. | T5/T12. Native pywebview bridge and installer are deferred; do not represent prototype access as the D2 bridge. |
| Course workspace | Course selection and optional saved meeting metadata. | T4/T5. Recurring calendar expansion and active-course suggestions are deferred pending scope approval. |
| Material importer | Text/Markdown and readable PDF with bounded extraction/page locations. | T6. PPTX and OCR are deferred; unreadable slides create no slide-backed claims. |
| Study engine / Ollama connection | One bounded local embedding/generation profile, course-scoped retrieval and checked guide/card output. | T7-T9. General quiz sets and multi-model optimization are deferred; semantic retrieval stays in the core proposal. |
| Practice/review / Local data store | Saved supported cards, reveal, again/good ratings, due dates, source control and portable export. | T4/T9/T10. Full D2 Attempt/feedback extensions and archive restore are not promised. |
| Lecture assistance | Original note capture remains available beside source material. | T1 documents deferral of automatic organization, gap suggestions and follow-up feedback; this leaves part of US-05/UC-01/AC-01.1 incomplete and requires explicit approval. |
| Notifications / Logging / Configuration/setup | Bounded in-app progress/errors, local metadata-only diagnostics and consent/model readiness. | T5/T7/T12. No push service or telemetry is introduced. |
These estimates assume reuse of the existing prototype and a small self-authored test library. They are not a full D2 implementation estimate or a measured velocity. If the advisor requires every D2 feature by April, the plan is infeasible at the stated availability and must be re-estimated rather than relabeled complete.

## 2. Milestones List (Assignment 6)

Complete artifact means the named file exists in the inspected history; it does not certify portal submission, grading, advisor approval, or completed peer review. Dates marked proposed are internal recovery/implementation targets. Course-week labels follow the syllabus; I do not infer unknown Canvas due dates from week numbers.

| ID / milestone | Date basis / status | Completion date | Demonstration, verification and verifier |
| --- | --- | --- | --- |
| C01: Week 1: team roster and signed contract | 2026-09-03 official syllabus date; Missing evidence; no signed contract found | 2026-11-25 recovery target / T1 | Find signed roster/contract or record unresolved requirement; I verify file; instructor assesses submission. |
| C02: Week 2: topic, biography, and reflection | Official week only; artifact evidence 2026-09-09; Topic/biography complete as artifacts; reflection not found | 2026-11-25 missing-item audit / T1 | Project-Description.md and bios/Jason-Galanie.md exist; I audit missing reflection and instructor submission evidence. |
| C03: Week 3: advisor and constraints essay | Official week only; exact due date unavailable; Open; advisor/constraints evidence not found | 2026-11-25 audit / T1 | Record advisor acceptance and constraints essay location; I collect evidence; advisor verifies topic/scope when available. |
| C04: Week 4: user stories and use cases | 2026-09-28 artifact date; Complete artifact; portal submission unverified | 2026-09-28 actual artifact | User_Stories.md and elicitation notes at 449f625; I verify stories/ACs; instructor grades submitted work. |
| C05: Week 5: high-level D0 | 2026-10-28 artifact date; official due date unavailable; Complete artifact; portal submission unverified | 2026-10-28 actual artifact | D0 PDF/Markdown/editable figures at 980a12d; I verify interfaces/figures; instructor grades. |
| C06: Week 6: detailed D1 | 2026-10-08 supplied assignment deadline; Complete artifact; first commit 2026-10-29; refreshed 2026-11-18 | 2026-11-18 current artifact | D1 model, algorithm, API and technology sections at c3e6986; I verify matching PDF/source; no on-time claim. |
| C07: Week 7: D2 and peer design review | 2026-10-14 supplied assignment deadline; Draft; actual peer feedback still missing | 2026-11-25 conditional recovery / T1 | D2 and Peer_Review_Notes.md at 33c4cc2; review is complete only with real teams/comments and applied must-fix actions. |
| C08: Week 8: Assignments 5/6 planning package | 2026-10-28 supplied assignment deadline; Draft on 2026-11-18; owner estimate review pending | 2026-11-25 proposed baseline / T1 | Tasklist.md, Planning sources, this PDF, matched IDs/hours/dependencies; I confirm estimates; advisor/instructor review plan. |
| C09: Week 9: requirements and technical specification | Official week only; exact due date unavailable; Remaining; dedicated final artifacts not found | 2026-11-25 proposed recovery / T1 | Requirements/technical specification map to D0-D2 and scoped release; I verify coverage; advisor/instructor assess. |
| C10: Week 10: test plan draft | Official week only; exact due date unavailable; Remaining; dedicated test-plan file not found | 2026-11-25 proposed recovery / T1 | List acceptance checks, fixture inputs, expected outputs and release gates; I verify testability; instructor reviews. |
| C11: Week 11: ethics and responsible use | 2026-11-11 artifact date; official deadline unverified; Complete artifact; signed copy previously verified; submission unverified | 2026-11-11 actual artifact | Ethics_Statement.md, NOTICE.md and MIT LICENSE; I verify consistency; instructor grades actual submission. |
| C12: Week 12: presentation draft and advisor feedback | Draft target proposed; advisor feedback not yet obtained; Remaining / T2 | 2026-11-23 proposed draft | Five-minute walkthrough with sources, limitations and timing; I rehearse; advisor feedback must be recorded rather than invented. |
| C13: Weeks 13-14: oral presentation slot | 2026-11-25 supplied presentation schedule; Scheduled; not yet delivered / T2 | 2026-11-25 scheduled event | Updated CS5001 presentation schedule lists my name on Day 3; I deliver; instructor verifies the five-minute slot. |
| C14: Week 14: design report, notebook, team/self assessment | Exact official deadline unavailable; Remaining / T3 | 2026-12-04 proposed handoff target | Final report reproduces task/timeline/effort tables; notebook contains actual hours; I verify artifacts; instructor assesses. Confirm deadline in Canvas. |
| I00: Spring scope and environment kickoff | Internal target; scope approval required; Planned / T1,T4 | 2027-01-11 | Review confirmed availability/estimates, approved deferrals and baseline commit; I record decisions; advisor approves changed release scope. |
| I01: Persistent capture and source-navigation checkpoint | Internal checkpoint; Planned / T4,T5 | 2027-01-29 | Save/restart a note in its course and open its original source; I run fixture and retain test log; advisor can reproduce. |
| I02: Readable imports and local model setup checkpoint | Internal checkpoint; Planned / T6,T7 | 2027-02-12 | Import readable PDF with page link; unreadable PDF produces no slide claims; local model readiness/consent/errors are visible. I verify. |
| I03: Course-scoped semantic retrieval checkpoint | Internal checkpoint; Planned / T8 | 2027-02-26 | Search permission-cleared course fixtures, reject wrong-course/digest results and record target-laptop latency. I verify; no unmeasured speed claim. |
| I04: Core alpha walkthrough | Major internal milestone; Planned / T4-T10 | 2027-03-12 | Save/import -> retrieve -> checked draft -> accept -> practice -> evidence -> delete/export works on fixtures; I demonstrate. Broader T11 fault checks remain explicit. |
| I05: Integration and failure-recovery checkpoint | Internal checkpoint; Planned / T11,T12 | 2027-03-26 | Record passing empty/bad model/wrong-course/stale citation/deletion/restart checks and any unresolved failures; I verify with saved evidence. |
| I06: Usable beta | Major internal milestone; Planned / T11,T12,T13 | 2027-04-02 | Core checks plus keyboard/source-return and available screen-reader checks pass; I log remaining barriers; no external user feedback is claimed without it. |
| I07: Release candidate and report evidence freeze | Major internal milestone; Planned / T14,T15 | 2027-04-16 | Clean-account run or documented manual-setup fallback, dependency notices, evaluation counts and release instructions are recorded; I verify; advisor reviews. |
| I08: Final demo and implementation-semester handoff | Major internal target; course date unconfirmed; Planned / all spring tasks | 2027-04-23 | Reproduce core demo from documented installation and hand over source, tests, evaluation and actual effort log; I verify; advisor/instructor assess at their official slot. |
## 3. Table 1, Timeline (Assignment 6)

All dates use YYYY-MM-DD and America/New_York. Start/finish dates include each task's 20% contingency. FS means finish-to-start; dependencies are technical/approval prerequisites. The one owner is resource-leveled, so tasks with independent technical dependencies still consume separate time slots. A same-day finish/start uses ordered, non-overlapping time allocations in Daily_Allocation.csv. Protected dates have zero task allocation.

| Task ID | Task statement | Owner | Start date | Completion date | Dependencies |
| --- | --- | --- | --- | --- | --- |
| T1 | Specify release priorities and the requirements/test baseline for Course workspace, Local data store, Study engine, and deferred D2 components. | Jason Galanie | 2026-11-18 | 2026-11-25 | None / real review, dates, scope/estimate confirmation |
| T2 | Document Desktop interface and Course workspace walkthroughs for the scheduled fall presentation. | Jason Galanie | 2026-11-18 | 2026-11-25 | None / confirmed Nov 25 slot |
| T3 | Document the Course workspace and Study engine design, notebook, and implementation handoff in the Week 14 report. | Jason Galanie | 2026-11-30 | 2026-12-02 | T1, T2 |
| T4 | Develop Local data store migrations, source ownership, immutable note revisions, and citation lookups for the core study flow. | Jason Galanie | 2027-01-11 | 2027-01-20 | T1 |
| T5 | Develop Desktop interface and Course workspace capture, course selection, job status, and source navigation in the existing local prototype. | Jason Galanie | 2027-01-21 | 2027-01-28 | T4 |
| T6 | Develop Material importer handling for text, Markdown, and readable PDFs with bounded extraction and page references. | Jason Galanie | 2027-01-29 | 2027-02-05 | T4, T5 |
| T7 | Develop Configuration/setup and Ollama connection checks for consent, installed local models, timeouts, and typed errors. | Jason Galanie | 2027-02-08 | 2027-02-12 | T4 |
| T8 | Develop Study engine passage embeddings and exact course-scoped semantic retrieval against a bounded fixture library. | Jason Galanie | 2027-02-15 | 2027-02-22 | T6, T7 |
| T9 | Develop Study engine generation and Practice/review for checked study guides, flashcards, answer reveal, and self-rating. | Jason Galanie | 2027-02-23 | 2027-03-01 | T8, T5 |
| T10 | Develop Local data store source deletion and portable export with dependent-item cleanup and recovery checks. | Jason Galanie | 2027-03-02 | 2027-03-05 | T4, T9 |
| T11 | Test Material importer, Study engine, and Local data store for integrated capture, retrieval, draft provenance, practice, and deletion flows. | Jason Galanie | 2027-03-08 | 2027-03-10 | T5, T6, T7, T8, T9, T10 |
| T12 | Test Access boundary, Logging, and Local data store for privacy, request validation, restart, and failure recovery. | Jason Galanie | 2027-03-22 | 2027-03-24 | T11 |
| T13 | Validate Desktop interface and Practice/review keyboard access, spoken labels, status announcements, and source-return focus. | Jason Galanie | 2027-03-25 | 2027-03-30 | T5, T9, T11, T12 |
| T14 | Validate Configuration/setup and Desktop interface installation on a clean Windows account with a documented manual setup fallback. | Jason Galanie | 2027-03-31 | 2027-04-06 | T7, T11, T12 |
| T15 | Document Study engine evaluation, Local data store limitations, release instructions, and the final demonstration evidence. | Jason Galanie | 2027-04-12 | 2027-04-14 | T11, T13, T14 |
### Table 1 milestone rows

| Milestone ID | Planned / recorded completion date | Dependencies / date status |
| --- | --- | --- |
| C01 | 2026-11-25 recovery target / T1 | Missing evidence; no signed contract found; 2026-09-03 official syllabus date |
| C02 | 2026-11-25 missing-item audit / T1 | Topic/biography complete as artifacts; reflection not found; Official week only; artifact evidence 2026-09-09 |
| C03 | 2026-11-25 audit / T1 | Open; advisor/constraints evidence not found; Official week only; exact due date unavailable |
| C04 | 2026-09-28 actual artifact | Complete artifact; portal submission unverified; 2026-09-28 artifact date |
| C05 | 2026-10-28 actual artifact | Complete artifact; portal submission unverified; 2026-10-28 artifact date; official due date unavailable |
| C06 | 2026-11-18 current artifact | Complete artifact; first commit 2026-10-29; refreshed 2026-11-18; 2026-10-08 supplied assignment deadline |
| C07 | 2026-11-25 conditional recovery / T1 | Draft; actual peer feedback still missing; 2026-10-14 supplied assignment deadline |
| C08 | 2026-11-25 proposed baseline / T1 | Draft on 2026-11-18; owner estimate review pending; 2026-10-28 supplied assignment deadline |
| C09 | 2026-11-25 proposed recovery / T1 | Remaining; dedicated final artifacts not found; Official week only; exact due date unavailable |
| C10 | 2026-11-25 proposed recovery / T1 | Remaining; dedicated test-plan file not found; Official week only; exact due date unavailable |
| C11 | 2026-11-11 actual artifact | Complete artifact; signed copy previously verified; submission unverified; 2026-11-11 artifact date; official deadline unverified |
| C12 | 2026-11-23 proposed draft | Remaining / T2; Draft target proposed; advisor feedback not yet obtained |
| C13 | 2026-11-25 scheduled event | Scheduled; not yet delivered / T2; 2026-11-25 supplied presentation schedule |
| C14 | 2026-12-04 proposed handoff target | Remaining / T3; Exact official deadline unavailable |
| I00 | 2027-01-11 | Planned / T1,T4; Internal target; scope approval required |
| I01 | 2027-01-29 | Planned / T4,T5; Internal checkpoint |
| I02 | 2027-02-12 | Planned / T6,T7; Internal checkpoint |
| I03 | 2027-02-26 | Planned / T8; Internal checkpoint |
| I04 | 2027-03-12 | Planned / T4-T10; Major internal milestone |
| I05 | 2027-03-26 | Planned / T11,T12; Internal checkpoint |
| I06 | 2027-04-02 | Planned / T11,T12,T13; Major internal milestone |
| I07 | 2027-04-16 | Planned / T14,T15; Major internal milestone |
| I08 | 2027-04-23 | Planned / all spring tasks; Major internal target; course date unconfirmed |
### Capacity, contingency and protected time

Expected effort E=(O+4M+P)/6. Task contingency is 0.20E; it is reserved for rework, not extra scope. The matrix shows productive expected hours and contingency separately. Protected blocks are additional time and are not hidden in task estimates. In a protected block I may fix a gate-blocking defect, review evidence or recover a slipped task; I do not schedule new features there.

| Period / block | Treatment | Hours / effect |
| --- | --- | --- |
| Fall recovery, Nov 18-Dec 4 | Use at most the 8-hour upper end of my range, leveled across weekdays; T2 includes the actual Nov 25 five-minute delivery. | 11.4 task+contingency hours across T1-T3; no claim that external feedback is guaranteed. |
| Nov 24; Dec 3 | Protected day before presentation / proposed report handoff. | 1.6 h each; no planned task work. |
| Nov 26-29 | Thanksgiving no-work block. | No task allocation. |
| Dec 6-12; Dec 13-Jan 10 | Fall exams, then deliberately no winter-gap feature work. | No task allocation; the winter gap is a planning blackout, not an official holiday label. |
| Jan 18; Mar 15-21 | MLK holiday and spring break. | No task allocation. |
| Mar 11-12 | Protected before I04 alpha. | 2.4 h at the 6 h/week planning average. |
| Apr 1-2 | Protected before I06 beta. | 2.4 h. |
| Apr 15-16 | Protected before I07 release candidate. | 2.4 h. |
| Apr 22-23 | Protected before I08 final demo/handoff. | 2.4 h; baseline work must finish by Apr 21. |
| Apr 24-29 | Spring exam block. | No new implementation work. |
| Co-op rotations and personal exam dates | Not supplied; do not assume that no rotation/conflict exists. | Insert actual blackouts and regenerate before accepting the plan. |
The spring calendar contains 14 non-break workweeks (January 11-April 23); January 18 removes one weekday. At 6 h/week that is 82.8 h gross. Subtract 9.6 h of protected milestone blocks to leave 73.2 h for tasks. Spring tasks require 55.0 h expected + 11.0 h contingency = 66.0 h, leaving 7.2 h unassigned schedule headroom. Fall recovery hours are counted separately.

| Actual weekly availability | Spring hours after holiday and protected blocks | Comparison with 66.0 h task budget |
| --- | --- | --- |
| 4 h/week | 48.8 h | Short by 17.2 h: the baseline cannot finish unchanged; agree a reduced scope or later deadline. |
| 6 h/week proposed average | 73.2 h | Fits with 7.2 h headroom, conditional on reviewed estimates and no new unavailable weeks. |
| 8 h/week upper bound | 97.6 h | 31.6 h headroom; this is not permission to expand scope or assume 8 h every week. |
The controlling resource-constrained path is T4 -> T5 -> T6 -> T7 -> T8 -> T9 -> T10 -> T11 -> T12 -> T13 -> T14 -> T15 -> I07 -> I08. It includes serialized work by one owner even where technical dependency arrows could branch. It is the path to monitor, not a claim of zero float: the protected blocks and 7.2 h of general headroom are stated separately. A T1 approval delay can block I00/T4. Missing peer feedback is an external gate, not effort that can be solved by adding imaginary hours.

## 4. Table 2, Effort Matrix (Assignment 6)

Hours below are proposed estimates, not actual hours or owner-confirmed estimates. O=optimistic, M=most likely, P=pessimistic. P in the member column marks primary responsibility. With one member I carry 100% of every row; there are no invented collaborators or undisclosed contributor shares. Actual effort will be recorded separately in the design notebook, with date, task ID, work performed and hours.

| Task ID / same statement | O / M / P (h) | Jason Galanie (h; P) | 20% buffer (h) | Row total (h) |
| --- | --- | --- | --- | --- |
| T1: Specify release priorities and the requirements/test baseline for Course workspace, Local data store, Study engine, and deferred D2 components. | 2.0 / 4.0 / 6.0 | 4.0 P | 0.8 | 4.8 |
| T2: Document Desktop interface and Course workspace walkthroughs for the scheduled fall presentation. | 1.0 / 2.5 / 4.0 | 2.5 P | 0.5 | 3.0 |
| T3: Document the Course workspace and Study engine design, notebook, and implementation handoff in the Week 14 report. | 1.5 / 3.0 / 4.5 | 3.0 P | 0.6 | 3.6 |
| T4: Develop Local data store migrations, source ownership, immutable note revisions, and citation lookups for the core study flow. | 4.0 / 7.0 / 10.0 | 7.0 P | 1.4 | 8.4 |
| T5: Develop Desktop interface and Course workspace capture, course selection, job status, and source navigation in the existing local prototype. | 3.0 / 6.0 / 9.0 | 6.0 P | 1.2 | 7.2 |
| T6: Develop Material importer handling for text, Markdown, and readable PDFs with bounded extraction and page references. | 3.0 / 6.0 / 9.0 | 6.0 P | 1.2 | 7.2 |
| T7: Develop Configuration/setup and Ollama connection checks for consent, installed local models, timeouts, and typed errors. | 3.0 / 5.0 / 7.0 | 5.0 P | 1.0 | 6.0 |
| T8: Develop Study engine passage embeddings and exact course-scoped semantic retrieval against a bounded fixture library. | 3.0 / 6.0 / 9.0 | 6.0 P | 1.2 | 7.2 |
| T9: Develop Study engine generation and Practice/review for checked study guides, flashcards, answer reveal, and self-rating. | 3.0 / 5.0 / 7.0 | 5.0 P | 1.0 | 6.0 |
| T10: Develop Local data store source deletion and portable export with dependent-item cleanup and recovery checks. | 2.0 / 4.0 / 6.0 | 4.0 P | 0.8 | 4.8 |
| T11: Test Material importer, Study engine, and Local data store for integrated capture, retrieval, draft provenance, practice, and deletion flows. | 1.5 / 3.0 / 4.5 | 3.0 P | 0.6 | 3.6 |
| T12: Test Access boundary, Logging, and Local data store for privacy, request validation, restart, and failure recovery. | 1.5 / 3.0 / 4.5 | 3.0 P | 0.6 | 3.6 |
| T13: Validate Desktop interface and Practice/review keyboard access, spoken labels, status announcements, and source-return focus. | 2.0 / 4.0 / 6.0 | 4.0 P | 0.8 | 4.8 |
| T14: Validate Configuration/setup and Desktop interface installation on a clean Windows account with a documented manual setup fallback. | 1.0 / 3.0 / 5.0 | 3.0 P | 0.6 | 3.6 |
| T15: Document Study engine evaluation, Local data store limitations, release instructions, and the final demonstration evidence. | 1.0 / 3.0 / 5.0 | 3.0 P | 0.6 | 3.6 |
| COLUMN / ROW TOTAL | Not an effort column | 64.5 P | 12.9 | 77.4 |
The expected member-column total is 64.5 h; the contingency column adds 12.9 h, for 77.4 h across fall and spring. Protected blocks are excluded from this matrix because they are additional capacity reservations, not assigned productive task effort. No cross-member imbalance can be rebalanced with one member. I manage concentration risk through the reduced release proposal, weekly time checks, documentation and advisor-approved scope changes. A new member would require a new estimate/ownership agreement rather than an automatic split of these hours.

## 5. Work breakdown structure

Level 1 is the phase; level 2 is the task. Every Task List item appears exactly once below with its original statement and primary owner.

### Fall baseline

- T1: Specify release priorities and the requirements/test baseline for Course workspace, Local data store, Study engine, and deferred D2 components. Owner: Jason Galanie.

- T2: Document Desktop interface and Course workspace walkthroughs for the scheduled fall presentation. Owner: Jason Galanie.

- T3: Document the Course workspace and Study engine design, notebook, and implementation handoff in the Week 14 report. Owner: Jason Galanie.

### Core implementation

- T4: Develop Local data store migrations, source ownership, immutable note revisions, and citation lookups for the core study flow. Owner: Jason Galanie.

- T5: Develop Desktop interface and Course workspace capture, course selection, job status, and source navigation in the existing local prototype. Owner: Jason Galanie.

- T6: Develop Material importer handling for text, Markdown, and readable PDFs with bounded extraction and page references. Owner: Jason Galanie.

- T7: Develop Configuration/setup and Ollama connection checks for consent, installed local models, timeouts, and typed errors. Owner: Jason Galanie.

- T8: Develop Study engine passage embeddings and exact course-scoped semantic retrieval against a bounded fixture library. Owner: Jason Galanie.

- T9: Develop Study engine generation and Practice/review for checked study guides, flashcards, answer reveal, and self-rating. Owner: Jason Galanie.

### Reliability and control

- T10: Develop Local data store source deletion and portable export with dependent-item cleanup and recovery checks. Owner: Jason Galanie.

- T11: Test Material importer, Study engine, and Local data store for integrated capture, retrieval, draft provenance, practice, and deletion flows. Owner: Jason Galanie.

- T12: Test Access boundary, Logging, and Local data store for privacy, request validation, restart, and failure recovery. Owner: Jason Galanie.

### Validation and handoff

- T13: Validate Desktop interface and Practice/review keyboard access, spoken labels, status announcements, and source-return focus. Owner: Jason Galanie.

- T14: Validate Configuration/setup and Desktop interface installation on a clean Windows account with a documented manual setup fallback. Owner: Jason Galanie.

- T15: Document Study engine evaluation, Local data store limitations, release instructions, and the final demonstration evidence. Owner: Jason Galanie.

## 6. Risk register

These are proposed risk judgments for my review. High-impact capacity, dependency and holiday risks are visible in Table 1, its protected blocks and its prerequisite notes. Likelihood/impact are qualitative (Low/Medium/High), not measured probabilities. I review the register weekly and update the plan when a trigger occurs.

| ID / category | Likelihood / impact / strategy | Trigger and mitigation | Owner / timeline link |
| --- | --- | --- | --- |
| R1 / Team / capacity | High / High / Reduce | Trigger: 4-8 h/week may not sustain the proposed 6 h average. At 4 h, the scoped plan is short 17.2 h before April 23. Mitigation: Compare actuals weekly; if two weeks average <6 h or a task consumes its 20% contingency, seek advisor-approved scope/date change before starting the next task. Do not assume unpaid catch-up. | Jason Galanie; T1; all dates; per-task contingency and protected blocks |
| R2 / External / review and approval | High / High / Reduce | Trigger: Real D2 peer feedback, advisor approval, official remaining deadlines or estimate confirmation are absent at the baseline review. Mitigation: T1 records open items and obtains real evidence; keep I00 conditional. A draft is not approved scope, and no reviewer is invented. Escalate unresolved course dates before C13/C14. | Jason Galanie; T1; C07-C10; I00 |
| R3 / Technical / local inference | Medium / High / Reduce | Trigger: T7 cannot establish a local profile or T8 exceeds the expected retrieval budget/quality target on the demo laptop. Mitigation: Use bounded fixtures, one verified embedding profile and exact scan; record actual time/memory; preserve manual notes/cards. Any removal of promised semantic search needs scope approval. | Jason Galanie; T7/T8; I02/I03; Mar 11-12 buffer |
| R4 / Technical / parsing and evidence | Medium / High / Reduce | Trigger: PDF has zero text, invalid pages, corrupt content or missing/incorrect citations. Mitigation: Keep text/Markdown and readable PDF in scope; reject image-only/OCR work; save original notes; require page/quote fixtures and unsupported-output rejection. | Jason Galanie; T6/T9/T11; I02/I05 |
| R5 / Technical / setup and access | Medium / High / Reduce | Trigger: T14 cannot produce a repeatable clean-Windows run or safe access boundary within its estimate. Mitigation: Baseline is the existing loopback prototype, not an unverified desktop bridge. Bound access/requests in T5/T12; document Python-based manual setup if packaging fails; disclose limitation. | Jason Galanie; T5/T12/T14; Apr 15-16 RC buffer |
| R6 / Team/external / exams, breaks, co-op | High / High / Avoid | Trigger: Exam load, a new co-op rotation or unreported absence removes a planned work session. Mitigation: No feature work during Dec 6-Jan 10, Mar 15-21 or Apr 24-29; protect Thanksgiving/MLK and milestone blocks. Co-op dates are unknown; insert them and rerun capacity immediately when known. | Jason Galanie; Blackouts and daily capacity; R1 trigger |
| R7 / Technical / data loss and stale evidence | Medium / High / Reduce | Trigger: Restart/deletion/migration test loses a saved note or publishes a stale/unsupported draft. Mitigation: Keep small synthetic fixtures and backup before schema changes; block beta/release until T11/T12 recovery/provenance checks pass; use protected integration blocks rather than adding features. | Jason Galanie; T4/T9/T10/T11/T12; I04-I07 |
| R8 / External / validation access | Medium / Medium / Reduce | Trigger: No screen-reader reviewer or permitted student material is available by T13/T15. Mitigation: Use self-authored fixtures and direct keyboard/screen-reader checks; label missing stakeholder evidence and ask advisor about an acceptable validation method. Do not claim a user study or learning gain. | Jason Galanie; T13/T15; I06/I07 |
| R9 / Team / scope growth | High / High / Reduce | Trigger: Calendar, PPTX/OCR, native packaging or lecture-assistance work is requested before core acceptance checks pass. Mitigation: Keep the deferred-scope table visible. No new feature enters protected blocks; replace an equal-effort item only after owner/advisor approval and regenerate all planning tables. | Jason Galanie; T1 scope gate; I00; all major buffers |
### Evidence and baseline checks

The syllabus calendar supplies the Week 1-14 deliverable categories. The current repository supplies artifact dates/statuses; the supplied D1, D2 and planning assignments supply October 8, October 14 and October 28 deadlines. Both local copies of CS5001_Updated_Presentation_Schedule.docx list my November 25 slot. These sources do not prove that any file was submitted or that an advisor accepted the scope.

UC calendar sources: https://www.uc.edu/about/registrar/calendars/academic-year-calendars/2026-2027.html and https://www.uc.edu/about/registrar/calendars/spring-2027/dates-deadlines.html. These support the academic breaks/exam windows and January 11-April 23 class period, not course-specific capstone submission dates.

Before treating this as the final assessed plan, I need to confirm the per-task O/M/P estimates and risk priorities myself, obtain actual peer/advisor feedback, confirm the narrowed release scope and remaining Canvas/CS5002 deadlines, and add any co-op or personal exam conflicts. The assignment reserves those decisions to me; formatting assistance is not evidence that I already made them.
