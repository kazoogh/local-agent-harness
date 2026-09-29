# Local Study Assistant: scope, architecture, and roadmap

## Decision and Senior Design fit

**My decision: pursue the pivot**, subject to advisor approval of the changed topic. I see a concrete problem, an end-to-end demo, and engineering work I can evaluate. I want to focus on a bounded pipeline that turns a student's selected material into *traceable, editable retrieval practice*, with measurable failures and a working offline path.

I do not have a Senior Design syllabus, rubric, or advisor instructions in this repository yet. I am currently working alone and have not selected an advisor. I am treating this plan as proposed requirements, not a statement of course-specific grading. UC's published CS outcomes emphasize designing, implementing, and evaluating a computing solution; I will confirm exact deliverables and the topic change with my advisor ([UC CS accreditation outcomes](https://www.ceas.uc.edu/about/accreditation/abet/computer-science.html)).

## Users and core problem

I am designing primarily for a student working across several courses with rough notes and instructor-provided material. I want a quick capture to remain useful before it is organized. During class, the student should be able to upload the professor's slides and spend their time noting extra explanations and their own questions instead of copying slides. The assistant could keep those notes beside the relevant slides, help organize them, and ask a short question with evidence-based feedback. My aim is to support active recall alongside reading, lectures, and academic judgment.

I looked at the Learning Space in my portfolio repository as a workflow reference. It already has a capture box, optional course choice, recent notes, material upload, private sync, AI note expansion, and review prompts. I am keeping this capstone in a separate repository and concentrating on the local, evidence-aware generation and evaluation path. I will use the product lessons from my portfolio work while making the technical contribution of this project clear.

## Bounded MVP and demo

1. Create a course or use an inbox; capture a rough note without forcing classification.
2. Import text or Markdown material and show the exact source used for each generated item. Add PDF page extraction only after text flow is stable.
3. Ask a local model to draft cards and short practice questions from selected material. Keep a working manual path when the model is absent or fails.
4. Reject structurally invalid or unsupported drafts; show source excerpts and let the student edit, accept, or discard candidates.
5. Run a short recall session, reveal the expected answer and evidence, collect the student's rating, and schedule the next review transparently.
6. Export and delete local data before testing with real student material.

For the next slice after the text workflow, I want an opt-in lecture mode: import slides with page or slide locations, capture the student's notes about what the professor says beyond those slides, help organize a rough note using the selected slide as context, and ask a single follow-up question. The student should be able to accept, edit, defer, or dismiss each suggestion. The assistant must keep the student's original words separate from slide-backed details and its own inferences; it cannot know every point the instructor said or predict what will be on an exam.

**Demo script:** capture an imperfect lecture thought; add a short permitted course handout; ask for cards; show a rejected unsupported answer and a supported card; edit and accept it; answer from memory; reveal its source; rate recall; view the next due date; delete the source and confirm dependent cards are removed. The current prototype covers this sequence for cards, except the model-dependent steps require a local model and export remains future work.

**Out of scope for MVP:** an autonomous desktop agent, multi-user cloud sync, LMS/calendar integration, automatic web research, large textbook ingestion, audio/video transcription, automatic grading of free-text answers, institutional deployment, and a broad adaptive tutoring model. Quizzes and feedback beyond flashcard self-rating follow after the citation and data-handling foundation is proven.

## Architecture

I am targeting a downloadable desktop application with settings for model selection and study preferences. I built the current loopback web prototype to test the core workflow before choosing a desktop shell or installer. Open-source users may edit the code, but I want ordinary configuration to work without source edits. I still need to test packaging and model setup on a clean student computer.

```text
Loopback browser UI
  ├─ quick text capture / .txt or .md import
  ├─ source selection and editable draft cards
  └─ recall and self-rating
           │ JSON, same origin
Python loopback server (127.0.0.1)
  ├─ SQLite: courses → sources → cards → reviews
  ├─ quote/answer validation and scheduling
  └─ explicit request → local Ollama model → validated candidates
```

The server does not need a cloud account or API key. A model call is user-triggered and sends only the selected source excerpt to a configured loopback Ollama endpoint. A student must choose a downloaded local model to keep inference local; Ollama can also route to cloud models if configured for them. No general-purpose file, browser, or shell tools are exposed to the model. This retains the prior harness idea of *controlled* model action while reducing risk and implementation scope. The current validator requires the answer to be an exact substring of a quote that occurs in the selected source. This proves traceability, **not** factual correctness, question quality, or that the quote logically entails the answer. Human review and later evaluations address those limits.

For lecture assistance, I plan to extend this pipeline: extracted slide spans with page or slide IDs, a saved original note, a comparison request, proposed additions with exact source links, then a short question-and-feedback exchange. Suggestions will remain separate from the original capture until the student accepts or edits them. The assistant should label what came from slides and what is its own inference, and it should stay quiet during class unless the student enables or requests a check.

The browser renders student material as text, not HTML. SQLite foreign keys cascade from a deleted source to its cards and review events. The server is bound to loopback, restricts Host/Origin, accepts bounded JSON bodies, and only serves named static files. This is a single-user prototype; it must not be exposed on a network or represented as an account-isolated service.

## Requirements and evaluation

| Requirement | Evidence to collect |
| --- | --- |
| Fast capture | Time a new user from launch to saved note; test with a rough one-sentence capture. |
| Evidence traceability | For each card, verify that the displayed quote is in the selected source and the answer is in that quote. |
| Grounding quality | Manually label a small, permission-cleared set for answer support and usefulness; report precision and failure examples separately. |
| Lecture gap suggestions | Use labeled note-and-slide fixtures; count supported missing concepts found, unsupported suggestions, and missed concepts. |
| Interactive feedback | Check that each question and expected answer links to the selected source, and record whether feedback addresses the student's answer without changing the original note. |
| Student control | Demonstrate editing, accepting/rejecting drafts, source deletion, and eventually export. |
| Practice workflow | Demonstrate answer reveal, self-rating, due-date update, and retrieval after restart. |
| Privacy | Verify loopback-only listening, no default provider calls, ignored local database, and deletion cascade. |
| Reliability | Test invalid input, bad model output, model unavailable, empty source, and larger documents. |

For a pilot evaluation, I plan to label at least 20–30 candidate questions from self-authored or permission-cleared material using a simple rubric: supported answer, unambiguous question, and usefulness for recall. I will report counts and disagreements rather than claim a learning gain from a small pilot. If feasible, I will observe 3–5 students using their own permitted material, obtain consent, and avoid retaining raw course content in the report. I will compare manual card creation time with AI-assisted editing time and record model latency on the demo hardware.

## Privacy, copyright, and academic use

- Keep notes and material local by default. Disclose exactly when selected text is sent to a local model. If a cloud provider is ever added, require a separate opt-in and explain what text leaves the computer.
- Import only material the user is allowed to use; do not build a shared repository of textbooks, lecture files, or generated excerpts. Avoid copying long source passages into exported/shareable results.
- Provide deletion and portable export before use with real student materials; document backups, retention, and recovery when those features exist. Local storage still requires device security and may be included in the user's backups.
- Treat retrieved/course text as untrusted data, not commands to the model or application. Generated questions may be wrong even when they contain a real quote. Students review before practice and should follow course rules on AI assistance.
- Revisit institutional privacy requirements with an advisor before integrating an LMS, instructor roster, grades, or deployment to other students. The current prototype has none of these.

## Risks and mitigations

| Risk | Response |
| --- | --- |
| Model invents a plausible answer or bad question | Exact quote checks, human acceptance, labeled evaluation set, clear failure state. |
| Gap analysis mistakes slide content for everything said in class | Label suggestions as comparisons with selected slides and let the student dismiss them. |
| In-class prompts distract the student | Make checks opt-in and let students defer questions until later. |
| Exact-match validation rejects paraphrases | Keep it for the first safe slice; measure rejection rate and design a more careful entailment check later. |
| Long, scanned, or poorly formatted materials | Start with plain text; add bounded extraction and page-level provenance later. |
| Local model is slow or unavailable | Manual cards always work; record latency and test on target hardware. |
| Scope expands into an entire learning platform | Gate new features on demonstrated source-backed cards and review workflow. |
| Portfolio overlap obscures original work | Keep independent code and evaluate the evidence pipeline explicitly. |

## Roadmap

| Stage | Deliverable | Exit check |
| --- | --- | --- |
| 0 — proposal and slice (current) | Revised project scope; loopback capture, text import, validated card drafts, recall review. | Tests pass; demo works without an AI model and can use one when configured. |
| 1 — data control | Edit/reject/delete individual cards, export/import, schema migration path, recovery guidance. | No real student content used before export and deletion are verified. |
| 2 — richer sources | PDF and slide text extraction with page or slide references, document limits, visible extraction errors. | Every generated item cites a source location that can be opened. |
| 3 — interactive lecture help | Compare saved notes with selected slides, suggest supported additions, and offer an opt-in follow-up question with feedback. | Labeled fixtures show supported gaps; original notes remain intact; unreadable slides produce no gap claims. |
| 4 — practice generation | Short quizzes and practice questions with source-backed answer/rubric and formative feedback. | Ambiguous/unsupported questions can be rejected by the student; labeled quality evaluation is reported. |
| 5 — desktop packaging | Installable desktop shell, model setup guidance, and settings for local model selection. | A student can install and use the app on a clean computer without editing source code or buying an API key. |
| 6 — study evaluation | Usability observations, card-quality labeling, latency measurements, presentation/report. | State measured strengths and failure cases honestly; advisor requirements met. |

## Open decisions for advisor review

I need to confirm the formal topic/title change, required artifacts and dates, whether individual projects are allowed, evaluation and participant rules, and available demo hardware. These decisions do not block my current prototype work.
