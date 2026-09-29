# Local Study Assistant

I am Jason Galanie, and this is my Senior Design project. My working team name remains **Local Agent Systems**. I am building a study assistant that lets students keep the professor's slides with their own notes about what was said beyond the slides, then turn that material into source-backed practice. Students keep control of their data and review AI suggestions.

## Current prototype

My first prototype is a single-user local web app. It saves rough captures, imports `.txt` or `.md` course material, drafts extractive flashcards with an optional Ollama model, requires human acceptance before practice, and schedules simple recall reviews. Students can also make cards manually when no model is configured. I still plan to add slide extraction, interactive note expansion, gap suggestions, follow-up questions, generated quiz sets, and richer feedback.

Requires Python 3.11 or newer. No Python packages or cloud account are required.

```powershell
python -m study_assistant.server
```

Open `http://127.0.0.1:8765`. Data is saved to `data/study.sqlite3`, which Git ignores. The server listens only on loopback. It is intended for one person on one computer and has no account system.

For optional AI card drafting, run [Ollama](https://ollama.com/) locally, download a local model, and set `STUDY_MODEL` to its installed model name before starting the server. The app contacts only `http://127.0.0.1:11434/api/generate`, and only after the **Draft with Ollama** button is pressed. It sends at most the first 12,000 characters of the selected source to Ollama. Choose a downloaded local model: Ollama can also run cloud models when configured to do so. All drafts require an exact quote containing the answer; the student still checks and accepts them.

```powershell
$env:STUDY_MODEL = "your-installed-model-name"
python -m study_assistant.server
```

Run checks with `python -m unittest discover -s tests -v`. To use a different database location, set `STUDY_DB_PATH` before starting the server.

## Project documents

- [Week 04 user stories and use cases](User_Stories.md): assignment submission and acceptance criteria.
- [Week 04 elicitation notes](docs/elicitation/week04.md): interview themes, competitive review, and remaining stakeholder contact.
- [Project description](Project-Description.md): current proposal and team information.
- [Scope, architecture, and roadmap](docs/study-assistant-plan.md): rationale, requirements, technical design, evaluation, risks, and milestones.
- [Professional biography](bios/Jason-Galanie.md): background and updated capstone focus.

My previous local agent harness proposal remains in Git history. I am carrying its useful ideas—local processing, controlled tool use, human approval, and result verification—into this focused learning application.
