# Ethics Statement

**Local Study Assistant · Local Agent Systems**

Jason Galanie · November 11, 2026

I am the sole team member and own all components.

## Privacy summary

I used my [D0 flows and interfaces](Design_Diagrams/D0_High_Level_Design.md) and [D1 data model and API](Design_Diagrams/D1_Detailed_Design.md) to map the planned flows, then compared them with my prototype at `8e95688`. I found no D2, separately labeled Week 9/10 materials, or Week 3 / Assignment #7 constraints essay in this repository.

### Current prototype data flows

I store the prototype data in a local SQLite database at `data/study.sqlite3` or the path set by `STUDY_DB_PATH`. I haven't added database encryption. OS file permissions govern disk access. The loopback API returns full course, source, and card records to callers that pass its request checks. I explain local storage and optional Ollama processing in the notice above the forms. Save/import and draft clicks are affirmative actions. The app records no separate consent receipt and gives no up-front retention schedule.

| Data item | Source | Purpose | Consent | Storage | Access | Retention |
| --- | --- | --- | --- | --- | --- | --- |
| Course name | Student | Organize library | Add course | DB | App/browser | DB lifetime |
| Course ID | App UUID | Link sources | Add course | DB | App/browser | DB lifetime |
| Source ID | App UUID | Open/delete/draft | Save/import | DB | App/browser | Source deletion |
| Source course ID | Student selection | Group source or Inbox | Save/import | DB | App/browser | Source deletion |
| Source title | Note prefix/file name | Find source | Save/import | DB | App/browser | Source deletion |
| Source content | Typed note/file text | Read and quote evidence | Save/import | DB | App/browser | Source deletion |
| Source kind | App/form | Label note or material | Save/import | DB | App/browser | Source deletion |
| Source created_at | System clock | Sort library | Save/import | DB | App/browser | Source deletion |
| Card ID | App UUID | Accept and review | Save draft | DB | App/browser | Source cascade |
| Card source ID | Selected source | Resolve evidence | Save draft | DB | App/browser | Source cascade |
| Card question | Student/AI | Practice prompt | Save draft | DB | App/browser | Source cascade |
| Card answer | Student/AI | Reveal answer | Save draft | DB | App/browser | Source cascade |
| Card quote | Selected text/AI | Verify source | Save draft | DB | App/browser | Source cascade |
| Card status | App/accept click | Gate practice | Save/accept | DB | App/browser | Source cascade |
| Card due_at | App clock/scheduler | Queue next review | Save/rate | DB | App/browser | Source cascade |
| Card interval_days | App scheduler | Space recall | Save/rate | DB | App/browser | Source cascade |
| Card created_at | System clock | Sort cards | Save draft | DB | App/browser | Source cascade |
| Review ID | App UUID | Identify rating event | Rate recall | DB | App | Source cascade |
| Review card ID | Current card | Link event to card | Rate recall | DB | App | Source cascade |
| Review rating | Student button | Set interval | Rate recall | DB | App | Source cascade |
| Review reviewed_at | System clock | Record review time | Rate recall | DB | App | Source cascade |
| Original .txt/.md | File picker | Decode as text | Add material | Original on disk | OS/browser | App leaves original |
| Model availability | STUDY_MODEL set? | Enable Draft button | Local setup | Memory | App/browser | Process/page life |
| Model name | STUDY_MODEL | Select runtime model | Local setup + Draft | Memory | App/Ollama | Runtime-dependent |
| Prompt | First 12,000 source chars | Generate recall cards | Draft with Ollama | Memory | App/Ollama | Runtime-dependent |
| System instructions | App | Constrain draft format | Draft with Ollama | Memory | App/Ollama | Runtime-dependent |
| stream / format | App constants | Request one JSON result | Draft with Ollama | Memory | App/Ollama | Request |
| Model response | Ollama JSON | Check candidates | Draft with Ollama | Memory | App/Ollama | Runtime-dependent |
| Suggested Q / A / quote | Validated response | Edit before saving | Draft with Ollama | Page memory | App/browser | Switch source/reload |
| HTTP headers/status/error | Browser/server | Validate and report | Request; no opt-in | Memory | App/browser | Request/page |
| Access log fields | Loopback IP, time, request line, status/size | Diagnostics | Automatic; no prompt | Stderr | Console operator | Session or redirected log |

<!-- pagebreak -->

### Proposed design data flows

D0 I1-I7 and D1 §§2-5 define these fields and recipients. The desktop bridge, managed files, calendar and embedding jobs are proposed. The prototype's explicit Draft button does not document consent for D0's proposed background indexing of imported content.

| Data item | Source | Purpose | Consent | Storage | Access | Retention |
| --- | --- | --- | --- | --- | --- | --- |
| Course ID/name, time zone, meeting rules, weekday/times/date range; session ID/course/date/start/end | Student, app (I1/I4) | Schedule and classify sources | Proposed course setup | Local DB | App/OS | Course deletion |
| Note ID/course/session/title/text/capturedAt/createdAt | Student, clock (I1/I4) | Keep dated original | Proposed save | Local DB | App/OS | Source/course deletion |
| Upload ID/course/session/name/media type/bytes | File picker (I1/I2/I4) | Import original and locate it | Proposed import | Managed file + DB | Importer/app/OS | Source/course deletion |
| Source ID/kind/hash/originalRef/logicalId/isCurrent/libraryRevision | Importer/store (I2/I4/I5) | Detect duplicates and track revisions | Derived on save/import | Local DB | App/OS | Explicit deletion; old revisions retained |
| Passage ID/source/course/ordinal/text/start/end offsets; location type/page/slide/note ID | Importer/store (I2/I5) | Retrieve passages and open originals | Derived on save/import | Local DB | App/OS | Source deletion |
| Action, operation, type, IDs, record, committed, resolved location | UI/workspace/store (I1/I4) | Route reads and writes | User action | Memory; records above | App | Request |
| Job ID/course/kind/state/progress counts/createdAt/library revision/model digests/error | Engine (I3) | Track work and detect stale jobs | Import or study trigger | Local DB / status in memory | App/OS | Job expiry unspecified |
| Task scope/topic/count/k and practice item ID/answer; feedback | Student and engine (I1/I3/I5) | Select evidence and practice | Proposed study/practice action | Memory; answer persistence unspecified | App/engine | Unspecified |
| Settings: generation/embedding IDs, localOnly | Setup UI (I1) | Select local models | Proposed setup choice | Local settings | App/OS | Unspecified |
| Search input text/query vector and ranked IDs/scores/passages, readiness, affected IDs | Engine/store (I5) | Find course evidence | Triggered by study/index | Memory | Engine/store | Request/job |
| Embedding passage/section ID, model digest, dimension, vector, normalized/ready | Ollama and engine (I5-I7) | Search semantically | Background indexing; opt-in unspecified | Local DB | App/OS | Source removal; model change invalidates old index |
| Model operation, model, texts/input, instructions/system, prompt, stream/format/truncate | Engine/adapter (I6/I7) | Embed text or generate drafts | Index trigger or study action | Request memory | App/Ollama | Runtime-dependent |
| Returned model ID, text/response, done, vectors/embeddings | Ollama (I6/I7) | Validate outputs and store valid vectors | Same as request | Memory; accepted records in DB | App/Ollama | Request; persisted records follow source rules |
| Item ID/job/kind/question/answer/status; citation item/passage IDs, quote offsets, exact quote/location | Engine/student (I1/I3/I4) | Review and open supporting material | Study action; accept to activate | Local DB | App/OS | Deleted course; missing evidence invalidates item |
| Covered source IDs, warnings, status, error code/message/retryable, Result ok/data | Importer/engine/store (I1-I7) | Explain coverage, failures, next steps | Associated action | Memory or job record | App/OS | Job retention unspecified |

**Privacy and retention (ACM §1.6).** My prototype asks the student to click before model drafting. D0 proposes background indexing, and I still need to define its consent prompt. Confirmed source deletion cascades to cards and reviews in SQLite. I will use synthetic demo material where possible and keep demo data through final grading. After grading, I will stop the app and manually delete the demo database, sidecar files, and project-owned copies in managed files, indexes, exports, logs, and backups. Students keep their originals and control their own libraries. My prototype collects no sensor readings, account records, or grades. I haven't documented removing a field.

<!-- pagebreak -->

## Security summary

| Capstone gap | Implementation and audit evidence |
| --- | --- |
| Default credentials | No application accounts, passwords, setup credentials, API keys or session tokens. Token lifetime is therefore inapplicable. OS permissions apply to the file on disk. |
| Unauthenticated endpoints | The prototype binds to `127.0.0.1:8765`. It checks Host and Origin (absent Origin is permitted), requires JSON POST bodies and returns JSON with no-store. These checks restrict browser requests. The API still lacks caller authentication, including the state endpoint and write endpoints. The D1 design specifies a trusted desktop bridge and OS account boundary. That bridge is pending. |
| Secrets in source control | `STUDY_MODEL` and `STUDY_DB_PATH` are environment configuration values, and no app secrets are needed. `data/` is ignored. An override path elsewhere does not inherit that ignore rule. |

**Transport and load.** The app and Ollama use plain HTTP on loopback. There is no HTTPS or request rate limiter. The POST body limit is 300,000 bytes and the Ollama request has a 45-second timeout. The model client disables proxies and redirects. Loopback limits direct network exposure. The app cannot establish from its configuration that Ollama is running a downloaded model rather than using a cloud-backed model.

**Git history audit, November 11, 2026.** I used a pattern scan covering all seven commits reachable from local branches, remote-tracking refs and tags through `8e95688`. It searched 30 unique historical blobs, including extracted text from both PDFs, for private key markers, common provider token formats, credentials in URLs, likely literal secret assignments and sensitive file names. The scan found zero matches, so I made no credential-removal changes. The scan cannot detect arbitrary secrets, unreachable objects, or text embedded in images. Six existing tests passed, including SQLite cascade deletion and exact-quote validation with a controlled local model response.

### Self-audit

| Question | Answer and evidence |
| --- | --- |
| Can another local process read or modify app data? | The API has no process or user authentication. A local caller that passes request checks can read or write through it. OS file permissions separately govern database-file access. |
| What stops unsupported model drafts from entering practice? | `ai.py` and `store.py` validate exact quotes and answer inclusion. The student must save and then accept each card. This checks provenance. The student still needs to judge correctness. |
| Does upload content execute in the browser? | Prototype imports text/Markdown and displays content with textContent. Static pages restrict scripts and styles to self. PDF/PPTX parsing is a D2 item. |
| What happens when evidence is deleted? | Confirming source deletion removes its source row, cards and review history through foreign keys. The original selected file remains on disk. The current tests cover the database cascade. |
| Is local inference enforced end to end? | The app sends to a fixed loopback URL. README and UI tell the user to use a downloaded model. The server does not verify that model's execution mode. |
| What is the accessibility evidence? | Forms have labels, native controls and a live status region. D0 calls for keyboard and screen-reader testing. No such validation result was found in the repo. |

**Security and accessibility (ACM §§1.2, 1.4 and 2.9).** I designed the app for a single student using their own computer. My D1 design keeps the app bridge on trusted desktop pages and relies on the OS account. D0 calls for keyboard and screen-reader users to be able to open a source link and return to practice. I haven't documented a test of that workflow. [ACM Code of Ethics](https://www.acm.org/code-of-ethics)

<!-- pagebreak -->

## Licensing summary

I built this inventory from the tracked imports, browser asset references, model configuration, test fixtures and [D1 §§4 and 6](Design_Diagrams/D1_Detailed_Design.md). No dependency manifests, vendored libraries, model weights, or assets directory are tracked. License identifiers use the [SPDX License List](https://spdx.org/licenses/) and the actual upstream terms linked under Attribution.

| Component | Version / status | SPDX or rights | Type | Redistribution obligation |
| --- | --- | --- | --- | --- |
| CPython and standard library (incl. sqlite3, http.server, urllib, unittest) | 3.11+; tested 3.13.5 | Python-2.0 | Permissive | Preserve Python notices and license terms if bundled. Summarize changes to Python in distributed derivatives and carry incorporated software notices. |
| SQLite native library | Python-provided; tested 3.49.1 | Public domain; blessing in source | Public domain | No license conditions on upstream deliverable SQLite code. |
| Ollama runtime | Optional, separately installed; unpinned | MIT | Permissive | Carry copyright and permission notice if redistributed. Check bundled runtime components separately. |
| User-configured model | Optional; local name/tag set by user | Depends on weights | Varies | Verify chosen model's terms and exact artifact before redistribution. No weights ship in this repo. |
| Nomic Embed Text | D1 candidate v1.5; digest pending | Apache-2.0 | Permissive | Carry license and applicable notices, identify changes. Verify Ollama artifact. |
| Qwen3-4B | D1 candidate 4B; digest pending | Apache-2.0 | Permissive | Carry license and applicable notices, identify changes. Verify Ollama artifact. |
| NumPy | D1 candidate; unpinned | BSD-3-Clause | Permissive | Carry notice, conditions and disclaimer. No implied endorsement. Review binary notices. |
| tzdata / IANA data | D1 candidate; unpinned | Apache-2.0 / public domain | Permissive / public domain | Carry applicable notices for the package. Check data-file exceptions for the pinned release. |
| pywebview | D1 candidate; unpinned | BSD-3-Clause | Permissive | Carry notice, conditions and disclaimer. No implied endorsement. Verify platform webview terms. |
| PyInstaller | D1 candidate; unpinned | GPL-2.0-or-later WITH Bootloader-exception; Apache-2.0 runtime parts | Copyleft tool; bundling exception | Bootloader exception allows licensing a combined executable under app/dependency terms. Separate redistribution or modification requires checking the GPL terms. Carry applicable runtime notices. |
| pypdf | D1 candidate; unpinned | BSD-3-Clause | Permissive | Carry notices and disclaimer. No implied endorsement. |
| python-pptx | D1 candidate; unpinned | MIT | Permissive | Carry copyright and permission notice. |
| Platform browser and system font | User-installed; varies | Platform terms | External runtime | Repo ships neither the runtime nor the font. Check terms before packaging either. |
| D0/D1 drawings and PDFs; test fixtures | Tracked project files | MIT | Permissive | Keep the copyright and permission notice with copies or substantial portions. |
| Student notes and course files | User-provided; per upload | Rights depend on source | User content | Importing leaves existing rights intact. Keep course files out of the repo and release bundle. |

**Project license and compatibility.** I chose [MIT](LICENSE) for my original project code, documentation and fixtures so others can reuse and modify them. MIT is compatible with the prototype dependencies under the terms listed above. Bundled components and model weights keep their own terms. For D1 candidates, I will check the exact releases and include required notices. PyInstaller's bootloader exception permits an MIT-licensed app bundle under the applicable dependency terms.

<!-- pagebreak -->

## Attribution list

- [CPython and standard library](https://docs.python.org/3/license.html), Python Software Foundation and contributors, Python-2.0. [SQLite](https://sqlite.org/copyright.html), SQLite authors, public domain. [Ollama](https://github.com/ollama/ollama/blob/main/LICENSE), Ollama contributors, MIT.
- D1 candidates: [NumPy](https://github.com/numpy/numpy/blob/main/LICENSE.txt), [pywebview](https://github.com/r0x0r/pywebview/blob/master/LICENSE), and [pypdf](https://github.com/py-pdf/pypdf/blob/main/LICENSE), BSD-3-Clause. [python-pptx](https://github.com/scanny/python-pptx/blob/master/LICENSE), Steve Canny, MIT. [tzdata](https://github.com/python/tzdata/blob/master/LICENSE), Python tzdata maintainers, Apache-2.0 for the package and public-domain IANA data. [PyInstaller](https://pyinstaller.org/en/stable/license.html), PyInstaller Development Team, GPL with bootloader exception and Apache-2.0 runtime portions.
- Candidate models: [Nomic Embed Text v1.5](https://huggingface.co/nomic-ai/nomic-embed-text-v1.5) by Nomic AI and [Qwen3-4B](https://huggingface.co/Qwen/Qwen3-4B) by Qwen, Apache-2.0 at the upstream sources. Record the downloaded tag and digest before claiming the demo uses either artifact.
- The design documents credit me for the project diagrams and handouts. The UI requests the installed system font and ships no font file, icon pack, or third-party image. The exact OS font and its terms depend on the user's system.
- I found no adapted snippet identified in the tracked source or comments. I used [Learning Space on my portfolio](https://kazoo.gg/portfolio/) as a design reference.
- I don't bundle an external dataset. Student notes are typed directly and course material is imported from files the student selects. Uploading a file gives the app a copy of its text; permission to redistribute instructor materials or third-party content needs to come from the applicable rights holder. Tests use inline fixtures. Week 04 interview themes are summarized in [elicitation notes](docs/elicitation/week04.md), separate from runtime data.

The repository copy of this list is in [NOTICE.md](NOTICE.md).

## AI-use disclosure

> “Generative AI tools may be used for drafting and code assistance but not for the design decisions or written analysis that are assessed in this course.”

Codex is the only AI tool I use. The table records how I used it to prepare this statement. I also discussed licensing and retention options with Codex and chose MIT and manual post-grading cleanup.

| Tool | Used by | Task | Column | How verified |
| --- | --- | --- | --- | --- |
| Codex | Jason Galanie | Organize repository facts, draft and format the Markdown/PDF, and gather attribution links | Generally OK | Codex traced the draft to tracked source and D0/D1 and checked upstream terms against SPDX. |
| Codex | Jason Galanie | Assist with the Git history scan and run existing tests | Generally OK | I recorded the scan scope and results above. All six existing tests passed when Codex ran them. |

**Member confirmation**

I confirm that the project's architecture, data model, priorities, and design rationale were my own.

Jason Galanie · Signature __________________________ · Date ______________
