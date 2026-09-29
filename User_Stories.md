# Assignment 4 - User Stories and Use Cases

**Project:** Local Study Assistant (my proposed Senior Design pivot)  
**Team member:** Jason Galanie

## Where these ideas came from

I interviewed Kevin Chu, a fellow student, and Callie Galanie, my sister and a first-year college student. The shared problem was that professors give students slides or textbooks, but students still have to find their own ways to practice. Flashcards, questions, and a study guide based on class material would help. I also reviewed Quizlet and Anki as a second way to gather ideas; my notes are in `docs/elicitation/week04.md`.

The in-class note helper is my idea based on that problem. If I already have the professor's slides, I should not have to spend class copying them by hand. I want to jot down extra explanations the professor says, keep those notes next to the uploaded slides, and let the AI help organize them or ask a quick question. It should be clear which words came from my notes and which details came from the slides. I am also proposing an optional local Ollama model so the app does not require a paid API. I still need to confirm the project pivot with my advisor.

## Stakeholder map

| Category | Who | What matters |
| --- | --- | --- |
| Primary | Students, including Kevin and Callie | Easier note-taking alongside slides and more ways to practice afterward. |
| Secondary | Me, as the developer and maintainer | A downloadable app without a required hosted-model bill. |
| Hidden | Students who use screen readers | Being able to study without a mouse. This is a hypothesis I still need to check with one of those students. |

## User stories

**US-01 (primary):** As a college student studying for an exam, I want a guide based on my class material, so that I know which topics to review.

**US-02 (primary):** As a first-year college student, I want questions and feedback based on my course material, so that I can find out what I actually remember.

**US-03 (secondary):** As the app's maintainer, I want study generation to run on a student's computer, so that I do not have to pay for every study session.

**US-04 (hidden):** As a student who uses a screen reader, I want to complete a practice session with a keyboard and spoken labels, so that I can study independently.

**US-05 (primary):** As a student taking notes in class, I want to add the professor's extra explanations alongside the slides I already have, so that I can focus on what is new instead of copying the slides.

### INVEST check

I kept each story separate, left the exact interface open to change, and limited it to something I could build and test. Here is my quick check:

| Story | Value, size, and test |
| --- | --- |
| US-01 | A one-course guide helps with review; check that its topics point back to the selected material. |
| US-02 | One question-and-feedback exchange helps reveal a knowledge gap; check the feedback against the source. |
| US-03 | One local-model workflow avoids a hosted bill; run it without a paid API key. |
| US-04 | One keyboard-only practice session supports independent study; test it with a screen reader. |
| US-05 | One rough note beside one slide set is enough to test; check that the original note and slide source stay clear. |

## Use cases

### UC-01 - Take notes alongside lecture slides

**Expands:** US-05 (and supports US-02).  
**Primary actor:** Student taking notes.  
**Secondary actor:** Local model service.  
**Preconditions:** The student has a course, selected slides, and a running local model. The system checks whether it can read the slides.

**Main success flow**

1. **Student:** Opens the slides and writes a quick note about something the professor adds in class.
2. **System:** Saves the note alongside the slides and shows the related slide or page.
3. **Student:** Asks for help organizing the rough note.
4. **System:** Suggests a clearer version, keeping the student's words distinct from any slide details it adds or points out.
5. **Student:** Accepts or edits the suggestion and asks for a practice question.
6. **System:** Saves the revised note, keeps the original, and asks a question based on the note and slides.
7. **Student:** Answers the question.
8. **System:** Gives feedback and shows the expected answer with its slide or page reference.

**Alternate flow:** At step 5, the student chooses to practice later. The system saves the note without starting a question.  
**Exception flow:** At step 2, if the slides have no readable text, the system explains the problem and saves the student's note without adding slide details.  
**Postcondition:** The original note stays available beside the slides, with any accepted AI edits saved separately. If the slides cannot be read, the student's note is still saved.

## Given / When / Then acceptance criteria

**AC-01.1 (main flow):** Given a readable slide and a student's note about an extra point the professor made, when the student asks for help and answers a follow-up question, then the original note stays unchanged, any added slide detail has a slide reference, and the question feedback shows an expected answer with a note or slide reference.

**AC-01.2 (exception):** Given slides with zero extractable text, when the student saves a note and asks for help organizing it, then the note remains saved, zero slide-based details or questions are created, and the system says the slides could not be read.
