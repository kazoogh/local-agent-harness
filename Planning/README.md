# Planning source files

This package is a proposed plan dated 2026-11-18. The confirmed availability is 4-8 hours/week; 6 hours/week is a proposed scheduling average. The owner has not confirmed the task-level O/M/P estimates or the reduced release scope. Course-specific dates not present in the supplied materials are marked unconfirmed. D2 peer review is still pending.

- `../Tasklist.md`: the 15 required verb-first tasks and their primary owner.
- `Task_and_Milestone_Plan.md`: complete six-part planning document and schedule evidence.
- `Plan_Inputs.json`: the task estimate, ownership, priority, dependency and blackout snapshot used for this proposal.
- `Daily_Allocation.csv`: the corresponding ordered productive/contingency allocation. Same-day task handoffs do not overlap.
- `render_plan.py`: regenerates the formatted PDF from the reviewed Markdown using ReportLab.
- `Task_List_and_Project_Plan.pdf`: current rendered draft.

Review and revise estimates, scope, availability and unknown course dates before accepting this baseline. If an input changes, reconcile the task list, narrative, dates, matrix, allocation and totals together; the Markdown renderer formats the text and does not reschedule tasks. Record actual effort separately in the design notebook.

Run from the repository root: `python Planning/render_plan.py`. An alternate output folder can be supplied with `--output-directory`.
