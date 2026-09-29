"""Run with: python -m study_assistant.server"""

import json
import os
import sqlite3
from contextlib import closing
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import urlsplit

from . import ai, store


ROOT = Path(__file__).resolve().parent.parent
WEB = ROOT / "web"
DB_PATH = Path(os.environ.get("STUDY_DB_PATH", ROOT / "data" / "study.sqlite3"))
MODEL = os.environ.get("STUDY_MODEL", "").strip()
MODEL_ENDPOINT = "http://127.0.0.1:11434/api/generate"
MAX_REQUEST_BYTES = 300_000


class Handler(BaseHTTPRequestHandler):
    def _json(self, status: int, data: dict) -> None:
        body = json.dumps(data).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(body)

    def _allowed_origin(self) -> bool:
        host = self.headers.get("Host", "")
        if host not in ("127.0.0.1:8765", "localhost:8765"):
            return False
        origin = self.headers.get("Origin")
        return origin is None or origin == f"http://{host}"

    def _body(self) -> dict:
        if self.headers.get("Content-Type", "").split(";")[0] != "application/json":
            raise ValueError("Use application/json.")
        try:
            size = int(self.headers.get("Content-Length", "0"))
        except ValueError as exc:
            raise ValueError("Invalid request length.") from exc
        if size < 1 or size > MAX_REQUEST_BYTES:
            raise ValueError("Request is empty or too large.")
        try:
            data = json.loads(self.rfile.read(size))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise ValueError("Invalid JSON.") from exc
        if not isinstance(data, dict):
            raise ValueError("Expected a JSON object.")
        return data

    def do_GET(self) -> None:
        if not self._allowed_origin():
            self._json(403, {"error": "Local origin required."})
            return
        path = urlsplit(self.path).path
        if path == "/api/state":
            with closing(store.connect(DB_PATH)) as db:
                self._json(200, {**store.state(db), "model_available": bool(MODEL)})
            return
        files = {"/": ("index.html", "text/html"),
                 "/app.js": ("app.js", "text/javascript"),
                 "/style.css": ("style.css", "text/css")}
        if path not in files:
            self._json(404, {"error": "Not found."})
            return
        name, mime = files[path]
        content = (WEB / name).read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", mime + "; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Content-Security-Policy", "default-src 'self'; script-src 'self'; style-src 'self'")
        self.end_headers()
        self.wfile.write(content)

    def do_POST(self) -> None:
        if not self._allowed_origin():
            self._json(403, {"error": "Local origin required."})
            return
        path = urlsplit(self.path).path
        try:
            data = self._body()
            with closing(store.connect(DB_PATH)) as db:
                if path == "/api/courses":
                    result = store.create_course(db, data.get("name", ""))
                elif path == "/api/sources":
                    result = store.create_source(db, data.get("course_id") or None,
                                                 data.get("title", ""),
                                                 data.get("content", ""),
                                                 data.get("kind", ""))
                elif path == "/api/cards":
                    result = store.create_card(db, data.get("source_id", ""),
                                               data.get("question", ""),
                                               data.get("answer", ""),
                                               data.get("quote", ""))
                elif path == "/api/sources/delete":
                    store.delete_source(db, data.get("source_id", ""))
                    result = {"deleted": True}
                elif path == "/api/cards/accept":
                    store.accept_card(db, data.get("card_id", ""))
                    result = {"accepted": True}
                elif path == "/api/reviews":
                    result = store.review_card(db, data.get("card_id", ""),
                                               data.get("rating", ""))
                elif path == "/api/cards/draft":
                    if not MODEL:
                        raise ValueError("Set STUDY_MODEL to enable local AI drafting.")
                    source = db.execute("SELECT content FROM sources WHERE id = ?",
                                        (data.get("source_id", ""),)).fetchone()
                    if source is None:
                        raise ValueError("Source not found.")
                    result = {"cards": ai.draft_cards(source["content"], MODEL, MODEL_ENDPOINT)}
                else:
                    self._json(404, {"error": "Not found."})
                    return
            self._json(200, result)
        except (ValueError, TypeError) as exc:
            self._json(400, {"error": str(exc)})
        except sqlite3.Error:
            self._json(500, {"error": "Database error."})


def main() -> None:
    with closing(store.connect(DB_PATH)):
        pass
    server = HTTPServer(("127.0.0.1", 8765), Handler)
    print("Study assistant at http://127.0.0.1:8765")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
