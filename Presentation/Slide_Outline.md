# Slide Outline and Timing

Project: Local Study Assistant | Team: Local Agent Systems | Team member: Jason Galanie

Deck v0.1 draft, November 19, 2026. I present all slides. My chosen assignment target is 10 minutes (600 seconds); the 5-minute cut is contingency for the conflicting published schedule, not the primary plan.

| Slide | Title | Content cues | Visual | Speaker | Seconds | Optional 5-minute cut |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Local Study Assistant | Purpose, free local goal, scope | Purpose and goal statements | Jason Galanie | 35 | 20 |
| 2 | Team, contact, and advisor | Solo roster, institutional email, unresolved advisor | Single-owner responsibility | Jason Galanie | 25 | 15 |
| 3 | Project abstract | Local storage, editable drafts, source integrity | 100-word abstract with highlighted key terms | Jason Galanie | 60 | 30 |
| 4 | User stories and system design | US-05 notes; US-01 guide; US-04 access; D0 components | D0 redrawn as six editable component boxes | Jason Galanie | 85 | 50 |
| 5 | Major project constraints | Cost, solo capacity, security, legal; hardware trade-off | Four constraints tied to design decisions | Jason Galanie | 60 | 30 |
| 6 | Progress against the design | Prototype exists; documented design; evidence still needed | Three progress columns with explicit status | Jason Galanie | 60 | 30 |
| 7 | Expected end-of-term accomplishments | Fall deliverables first; Spring implementation staged | Fall outputs and Spring milestone sequence | Jason Galanie | 65 | 30 |
| 8 | Division of work and capacity | I own T1â€“T15; 55 core hours + 20% buffer | Task phases from the existing effort matrix | Jason Galanie | 65 | 25 |
| 9 | Expected Expo demonstration | Source-to-practice sequence and honest fallback | Six-step expected demo and fallback | Jason Galanie | 85 | 45 |
| 10 | Recording and Week 13 delivery | Solo presenter; OBS; ten-minute target; share and post | Recording plan with ownership and audio check | Jason Galanie | 60 | 25 |
| 11 | D1: full data-model reference | Reference only; open source figure for detailed inspection | Original full design diagram | Jason Galanie | 0 | 0 |
| 12 | D2: full data-extension reference | Reference only; open source figure for detailed inspection | Original full design diagram | Jason Galanie | 0 | 0 |
| 13 | D2: full import/error-flow reference | Reference only; open source figure for detailed inspection | Original full design diagram | Jason Galanie | 0 | 0 |
| 14 | D2: full job-lifecycle reference | Reference only; open source figure for detailed inspection | Original full design diagram | Jason Galanie | 0 | 0 |
| 15 | Timing, sources, and AI disclosure | Main talk 600 seconds; backup 0; AI assistance disclosure | Timing totals and source traceability | Jason Galanie | 0 | 0 |

Total main talk: **600 seconds**. Optional short cut: **300 seconds**. All five backups: **0 seconds**, used only if needed in Q&A.

The abstract is 101 words, as requested. Its two-column prose is an intentional exception to the rough 6-by-6 guideline; I kept 16-point type instead of shrinking it. New slide captions and footers use 14 points. Full original D1/D2 figures are compact backup references; the original SVG files and design PDFs are the detailed zoomable copies.

## Speaker notes and source cues

### 1. Local Study Assistant
Speaker: Jason Galanie | Target: 35 seconds.

I am designing Local Study Assistant to keep a student's course material, original notes, and study tools in one local workspace. My goal is to help students keep notes and make study materials on their own computer for free. The central promise is control: students can inspect the source, edit a generated draft, and choose what becomes a study item. This is a Fall design presentation. I have a starting prototype; the full source-backed design is my implementation plan.

Source: Design_Diagrams/D0_High_Level_Design.md; Constraints_Essay.md

### 2. Team, contact, and advisor
Speaker: Jason Galanie | Target: 25 seconds.

I am Jason Galanie, the only member of Local Agent Systems. I own the design, implementation, testing, documentation, and presentation work. My contact is galanije@mail.uc.edu. As of November 19, 2026, I have not selected an advisor. Advisor agreement, the team-table entry, and contract approval remain open; this deck does not imply that any of them has happened.

Source: Team_Contract.md; Advisor_Record.md; project roster

### 3. Project abstract
Speaker: Jason Galanie | Target: 60 seconds.

The abstract describes my intended release rather than claiming it is finished. The important terms are local storage, exact source references, acceptance, and validation. Local generation alone cannot guarantee a correct answer. I therefore require both a source check and a student decision before a draft becomes active. The hardware trade-off is also explicit: avoiding a paid service moves processing to the student's device. This makes a useful manual workflow essential. The current prototype gives me a small working starting point, while retrieval, immutable revisions, recovery, and clean-machine validation remain planned work.

Source: User_Stories.md; Constraints_Essay.md; Technical_Specification.md

### 4. User stories and system design
Speaker: Jason Galanie | Target: 85 seconds.

US-05 asks for original notes alongside lecture material. US-01 asks for a guide based on that material. US-04 asks for keyboard operation and spoken labels; that accessibility need is still a hypothesis requiring validation. In my redrawn D0, the desktop interface selects a course workspace. Material importer and study engine operate on course-owned data in the local store. The engine calls my Ollama connection component, which wraps an external local runtime. These are logical components; the first release reuses the local web interface, while a native shell is deferred. The source path matters as much as generation: a draft must point back to the original passage. Full D1 and D2 reference diagrams follow in backup slides.

Source: User_Stories.md US-01/US-04/US-05; Design_Diagrams/D0_Block_Diagram.svg

### 5. Major project constraints
Speaker: Jason Galanie | Target: 60 seconds.

Economic constraints require zero recurring API or hosting charges. That leads to local storage and optional locally installed models. Professional constraints are my four to eight hours a week as a solo developer. I prioritize a Windows source-backed study flow and defer the native shell, recurring calendar, and automatic lecture-note assistance. Security constraints require a single-user loopback API, allowed Host and Origin values, and logs without course text. Legal constraints limit the demo to my own or permission-cleared material, with separate checks on dependency and model licenses. The concrete tension is privacy and recurring cost against hardware capacity. My balance is local optional inference with manual notes and flashcards still useful when AI is unavailable.

Source: Constraints_Essay.md Economic / Professional / Security / Legal (Regulatory)

### 6. Progress against the design
Speaker: Jason Galanie | Target: 60 seconds.

The existing Python and SQLite prototype includes local notes, text and Markdown import, manual supported flashcards, acceptance, and practice with reveal and self-rating. Its optional Ollama path is a limited drafting starting point. My documents now describe D0 through D2, the constraints, requirements, technical specification, implementation plan, and test plan. The test plan has forty-four active procedures and seven deferred reservations. Every new procedure is marked Not Run; I am not presenting planned coverage as a passing result. PDF import, course-scoped semantic retrieval, immutable revision handling, robust recovery, and clean-machine validation are future work. Peer-review evidence, test-case exchange, and advisor feedback are also missing.

Source: README.md; study_assistant/; Requirements_Document.md; Test_Plan.md

### 7. Expected end-of-term accomplishments
Speaker: Jason Galanie | Target: 65 seconds.

For the end of this Fall term, I expect a traceable design and test baseline, a rehearsed presentation with a recorded video, and the Week 14 design report and implementation handoff. T1 covers the baseline, T2 the presentation, and T3 the report. The current plan places presentation work by November 25 and report preparation by December 2; those are planning targets rather than new official deadlines. I do not expect the finished release this Fall. Spring implementation begins with capture and source ownership in January, adds import and local model setup in February, and moves through retrieval, alpha, recovery, and validation. The proposed protected gates are March 12 alpha, April 2 beta, and April 23 handoff. Advisor and stakeholder validation remain needed.

Source: Tasklist.md T1â€“T3; Planning/Task_and_Milestone_Plan.md

### 8. Division of work and capacity
Speaker: Jason Galanie | Target: 65 seconds.

As the sole team member, I own every task, T1 through T15. My plan divides the work into the Fall baseline, core implementation, reliability and control, and validation and handoff. The expected effort is 9.5 hours for T1 through T3; 35 hours for T4 through T9; 10 hours for T10 through T12; and 10 hours for T13 through T15. Spring totals fifty-five expected hours plus eleven hours of contingency. I have confirmed four to eight hours a week, with six hours used as the planning average. The estimates and reduced scope are still a planning proposal, not evidence of advisor approval. I protect testing and handoff dates by deferring optional features before cutting verification.

Source: Tasklist.md; Planning/Plan_Inputs.json

### 9. Expected Expo demonstration
Speaker: Jason Galanie | Target: 85 seconds.

At Expo, I expect to show one small self-authored course library. I select a course and import a readable PDF, add an original note, ask for a guide or flashcards, and open a cited passage before accepting a draft. I then practice with answer reveal and self-rating. Finally, I export the course or delete a source and show the dependent-item cleanup. The exact citation step is the main trust demonstration. This sequence is a release target, not a claim that the current prototype can already do every step. If the model fails, I switch to saved, checked study items and demonstrate manual practice. If the full app fails, I play a local prerecorded walkthrough and show source fixtures. The recording does not exist yet, so preparing and verifying that fallback is an open item.

Source: Technical_Specification.md; Test_Plan.md; Planning T15

### 10. Recording and Week 13 delivery
Speaker: Jason Galanie | Target: 60 seconds.

I will present all slides and target a ten-minute recording. My recording plan uses OBS with desktop capture and my microphone; software setup and the audio test are still pending. Before the final take, I will record a short sample, play it back, and check volume, clipping, screen readability, and whether any private windows or notifications appear. The planned share location is a UC OneDrive folder with a viewer-accessible deck PDF and video link; the folder and permissions still need to be created and tested. I own posting both links to the Senior Design Team Table in Week 13. The assignment asks for ten minutes, which is my chosen target, but the published November 25 schedule lists a five-minute slot. I need the instructor to resolve that conflict, and I have a five-minute cut in the outline if needed.

Source: Assignment brief; course schedule; Planning T2

### 11. D1: full data-model reference
Speaker: Jason Galanie | Target: 0 seconds.

I keep this full original diagram as a backup reference. It is not part of the timed talk. The original SVG and design PDFs remain available in Design_Diagrams for zoomed inspection; this compact overview preserves all original relationships and labels.

Source: Design_Diagrams/D1_Data_Model.svg

### 12. D2: full data-extension reference
Speaker: Jason Galanie | Target: 0 seconds.

I keep this full original diagram as a backup reference. It is not part of the timed talk. The original SVG and design PDFs remain available in Design_Diagrams for zoomed inspection; this compact overview preserves all original relationships and labels.

Source: Design_Diagrams/D2_Data_Extensions.svg

### 13. D2: full import/error-flow reference
Speaker: Jason Galanie | Target: 0 seconds.

I keep this full original diagram as a backup reference. It is not part of the timed talk. The original SVG and design PDFs remain available in Design_Diagrams for zoomed inspection; this compact overview preserves all original relationships and labels.

Source: Design_Diagrams/D2_Import_Error_Flow.svg

### 14. D2: full job-lifecycle reference
Speaker: Jason Galanie | Target: 0 seconds.

I keep this full original diagram as a backup reference. It is not part of the timed talk. The original SVG and design PDFs remain available in Design_Diagrams for zoomed inspection; this compact overview preserves all original relationships and labels.

Source: Design_Diagrams/D2_Job_State_Machine.svg

### 15. Timing, sources, and AI disclosure
Speaker: Jason Galanie | Target: 0 seconds.

Main slide times: 35, 25, 60, 85, 60, 60, 65, 65, 85, 60 seconds. Total 600 seconds. All backup slides have a target of zero seconds. The optional five-minute cut is 20, 15, 30, 50, 30, 30, 30, 25, 45, 25 seconds, totaling 300. I used OpenAI Codex to help organize the slide draft, speaker notes, and supporting files. The source content comes from my existing project documents. No advisor feedback, product-test result, or recorded demo was created as evidence. I must review and be able to explain the deck before presenting it.

Source: Assignment brief; repo documents at baseline 34197fa
