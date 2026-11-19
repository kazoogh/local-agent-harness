# Project Constraints Essay

**Project:** Local Study Assistant

**Team:** Local Agent Systems

**Team members:** Jason Galanie

**Prepared:** November 19, 2026

## Economic

Economic constraints apply because Local Study Assistant must work without a paid subscription, paid API key, or hosted backend. I require $0 in recurring API and application-hosting charges, so my viable design uses local SQLite storage and optional downloaded models instead of a required cloud inference service. Keeping course content local favors privacy and avoids per-request charges, but it shifts storage and processing costs onto the student's computer, so manual notes and flashcards must remain usable without AI.

## Professional

Professional constraints apply because I am the project's only team member and can spend 4-8 hours per week on implementation. That limit makes the current Windows local prototype my starting point and requires me to defer recurring calendars, automatic lecture-note organization, and a native desktop shell until the source-backed study flow is validated. I have not selected an advisor, so the advisor's two-semester commitment, meetings at least every two weeks, and team-contract approval remain unresolved requirements rather than completed milestones.

## Security

Security constraints apply because this single-user Windows app stores students' notes, course files, and study answers on their own device. The release must bind its application API only to loopback, reject requests outside its Host and Origin allowlist, and avoid placing course text or model prompts in diagnostic logs. Because local storage and an operating-system account do not isolate this app from other programs running with the same user's privileges, I exclude shared remote access instead of claiming multi-user security.

## Legal (Regulatory)

Legal constraints apply because imported slides and reading excerpts may be copyrighted, so I will use self-authored or permission-cleared material for demonstrations and will not bundle course files with the release. My original code uses the MIT license, while reused libraries and model weights keep their own license and notice requirements. Before distributing an installer, I must check the exact dependency versions and model artifacts and retain their required notices, which limits what I can package even when the app itself is free.
