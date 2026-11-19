# Requirements and specification support

Baseline: Requirements_Document.md and Technical_Specification.md, version 1.0 review draft, dated 2026-11-19. Both source documents are in the repository root. No advisor is assigned and no advisor review has occurred; this is an explicit evidence gap, not an approval claim.

Requirements_Registry.json preserves the proposed IDs, statements, priorities, sources, verification descriptions and design mappings. Traceability.csv contains the exact five-column, 33-row matrix. TC-001 through TC-033 are reservations for the Week 10 test plan, not executed test results. REQ identifiers are new; D2 NFR identifiers retain their meanings. Update these support files with the Markdown when a reviewed requirement changes; never reuse an ID.

render_documents.py regenerates both PDFs from the root Markdown using ReportLab. Run `python Specifications/render_documents.py --output-directory <folder>`. Explicit page-break markers preserve the seven-page/eight-page layout. The renderer does not change requirements or assess compliance. Figure links point to existing D0-D2 files at the recorded repository baseline; no figures are duplicated.
