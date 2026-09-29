# Project Description

## Team Name

Local Agent Systems (working team name)

## Project Title

Local Study Assistant (working title)

## Team Members

| Name | Major | Email |
| --- | --- | --- |
| Jason Galanie | Computer Science | [galanije@mail.uc.edu](mailto:galanije@mail.uc.edu) |

I am currently the only team member, and I am open to adding another student who is interested in the project.

## Problem and Proposed Solution

Students often have the professor's slides already, yet spend class copying slide text instead of capturing the extra explanation the professor gives. Turning scattered slides and rough notes into useful practice also takes time, and generic AI study output can contain unsupported claims or omit where an answer came from. I plan to build a downloadable, open-source, local-first study assistant that keeps uploaded slides alongside a student's own notes about what was said beyond them. During class, I want the assistant to help organize those rough notes, clearly separate slide-backed details from what the student wrote, and ask short follow-up questions with feedback. Later, it can create editable, source-backed flashcards and practice questions. A review loop will show the original evidence, collect the student's assessment of recall, and schedule follow-up practice. I want the desktop release to support an optional locally run model such as Ollama, without requiring a hosted API subscription.

My technical focus is an evidence-aware generation pipeline: selected course content goes to a local model only after a deliberate user action; proposed note additions and generated answers carry source references; unsupported candidates are rejected; the student accepts or edits drafts before using them. I plan to evaluate citation validity, the quality of gap suggestions and questions, privacy behavior, and whether students can complete the capture-to-practice workflow.

I am using the Learning Space on my portfolio site as a reference for fast capture and course organization. In this repository, I am developing and evaluating the local study pipeline as a separate Senior Design deliverable. I am also keeping the original harness proposal's ideas about local processing, controlled model calls, human review, and output verification.

My [project plan](docs/study-assistant-plan.md) defines the bounded MVP, architecture, milestones, and known risks. My current prototype handles text/Markdown sources and flashcard recall. I plan to add other formats, full quizzes, and more detailed feedback in later milestones.

## Faculty/Industry Advisor

I have not selected an advisor yet. I will confirm the topic change, final scope, deliverables, and course-specific rubric with the assigned Senior Design advisor.
