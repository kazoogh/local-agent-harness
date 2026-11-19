"""Generate synthetic QA inputs only; this does not execute the application tests."""
from pathlib import Path
from datetime import datetime, timezone
import argparse, hashlib, json, uuid
from reportlab.pdfgen import canvas

NOTE = "Photosynthesis converts light energy into chemical energy."
ALIASES = {
    "CA": "11111111-1111-4111-8111-111111111111",
    "CB": "22222222-2222-4222-8222-222222222222",
    "SA": "33333333-3333-4333-8333-333333333333",
    "SB": "44444444-4444-4444-8444-444444444444",
    "NA": "55555555-5555-4555-8555-555555555555",
    "NB": "77777777-7777-4777-8777-777777777777",
    "P1": "00000000-0000-4000-8000-000000000001",
    "P2": "00000000-0000-4000-8000-000000000002",
    "P3": "00000000-0000-4000-8000-000000000003",
    "PB": "00000000-0000-4000-8000-000000000004",
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    out = args.output.resolve()
    if out.exists() and any(out.iterdir()):
        parser.error("Choose a new or empty fixture directory; existing files are never overwritten.")
    out.mkdir(parents=True, exist_ok=True)
    e1 = [1.0] + [0.0] * 767
    e2 = [0.0, 1.0] + [0.0] * 766
    seed = {
        "fixture_version": "1.0",
        "origin": "Self-authored synthetic QA material; no student/course originals.",
        "aliases": ALIASES,
        "NOTE": NOTE,
        "T0": "2027-03-01T12:00:00Z",
        "T0_epoch": int(datetime(2027, 3, 1, 12, tzinfo=timezone.utc).timestamp()),
        "D1": "sha256:fixture-embed-v1",
        "D2": "sha256:fixture-embed-other",
        "REMOTE": {"digest": "sha256:unverified", "localVerified": False},
        "courses": [{"id": ALIASES[k], "name": k, "timeZone": "America/New_York"} for k in ["CA", "CB"]],
        "sessions": [{"id": ALIASES[s], "courseId": ALIASES[c], "date": "2027-01-12", "startsAt": "2027-01-12T15:00:00Z", "endsAt": "2027-01-12T16:00:00Z"} for s, c in [("SA", "CA"), ("SB", "CB")]],
        "note": {"id": ALIASES["NA"], "courseId": ALIASES["CA"], "sessionId": ALIASES["SA"], "title": "N", "text": NOTE},
        "otherCourseNote": {"id": ALIASES["NB"], "courseId": ALIASES["CB"], "sessionId": ALIASES["SB"], "title": "Other course", "text": NOTE},
        "passages": [{"id": ALIASES[p], "sourceId": ALIASES[source], "courseId": ALIASES[course], "ordinal": ordinal, "text": NOTE, "location": {"type": "note", "noteId": ALIASES[source], "pageOrSlide": None}} for p, source, course, ordinal in [("P1", "NA", "CA", 0), ("P2", "NA", "CA", 1), ("P3", "NA", "CA", 2), ("PB", "NB", "CB", 0)]],
        "MC": {"question": "What energy is converted?", "answer": "light energy", "quote": NOTE},
        "D_OK": {"question": "What energy is converted?", "answer": "light energy", "references": [{"passageId": ALIASES["P1"], "quoteStart": 0, "quoteEnd": len(NOTE), "quote": NOTE}]},
        "HTML_JS": '<img src=x onerror="window.__qa_executed=true">',
        "Q": e1,
        "vectors": {"unit-x": e1, "unit-y": e2},
        "F2": [{"id": ALIASES[p], "courseId": ALIASES[c], "modelDigest": "sha256:fixture-embed-v1", "vectorRef": v} for p, c, v in [("P1", "CA", "unit-x"), ("P2", "CA", "unit-x"), ("P3", "CA", "unit-y"), ("PB", "CB", "unit-x")]],
        "F3": {"byteCounts": [20*1024*1024-1, 20*1024*1024, 20*1024*1024+1], "sectionCounts": [499, 500, 501], "characterCounts": [999999, 1000000, 1000001], "noteLengths": [0, 1, 100000, 100001], "stubRule": "Isolate each validator; keep other limits valid. Do not pretend a 20-MiB text input also satisfies the 1-M-character cap."},
    }
    (out / "seed.json").write_text(json.dumps(seed, indent=2), encoding="utf-8")
    for name, text in [("note.txt", NOTE), ("N100.txt", "N"*100), ("N100000.txt", "N"*100000), ("N100001.txt", "N"*100001)]:
        (out/name).write_text(text, encoding="utf-8")
    for name, text in [("readable.pdf", NOTE), ("empty.pdf", "")]:
        c = canvas.Canvas(str(out/name), pagesize=(612, 792), invariant=1)
        if text:
            c.setFont("Helvetica", 12)
            c.drawString(54, 720, text)
        c.showPage()
        c.save()
    (out/"corrupt.pdf").write_bytes(b"not a PDF\n")
    benchmark = []
    for course in range(5):
        cid = str(uuid.uuid5(uuid.NAMESPACE_URL, f"qa-course-{course}"))
        for ordinal in range(1000):
            benchmark.append({"id": str(uuid.uuid5(uuid.NAMESPACE_URL, f"qa-{course}-{ordinal}")), "courseId": cid, "ordinal": ordinal, "text": NOTE, "modelDigest": seed["D1"], "vectorRef": "unit-x"})
    (out/"F4_passages.json").write_text(json.dumps({"courses": 5, "passagesPerCourse": 1000, "vectorDimension": 768, "materializeVectorsFrom": "seed.json/vectors", "passages": benchmark}), encoding="utf-8")
    files = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(out.iterdir()) if p.is_file() and p.name != "manifest.json"}
    (out/"manifest.json").write_text(json.dumps({"fixtureVersion": "1.0", "sha256": files}, indent=2), encoding="utf-8")
    print(f"Generated synthetic inputs in {out}; no application tests executed.")


if __name__ == "__main__":
    main()
