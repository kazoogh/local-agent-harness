"""SQLite persistence for the single-user, loopback prototype."""

import sqlite3
import time
import uuid
from pathlib import Path


def connect(path: Path) -> sqlite3.Connection:
    path.parent.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(path)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA foreign_keys = ON")
    db.executescript("""
        CREATE TABLE IF NOT EXISTS courses (
            id TEXT PRIMARY KEY, name TEXT NOT NULL UNIQUE
        );
        CREATE TABLE IF NOT EXISTS sources (
            id TEXT PRIMARY KEY, course_id TEXT REFERENCES courses(id),
            title TEXT NOT NULL, content TEXT NOT NULL,
            kind TEXT NOT NULL CHECK(kind IN ('capture', 'material')),
            created_at INTEGER NOT NULL
        );
        CREATE INDEX IF NOT EXISTS sources_course ON sources(course_id, created_at DESC);
        CREATE TABLE IF NOT EXISTS cards (
            id TEXT PRIMARY KEY, source_id TEXT NOT NULL REFERENCES sources(id) ON DELETE CASCADE,
            question TEXT NOT NULL, answer TEXT NOT NULL, quote TEXT NOT NULL,
            status TEXT NOT NULL CHECK(status IN ('draft', 'active')),
            due_at INTEGER NOT NULL, interval_days INTEGER NOT NULL DEFAULT 0,
            created_at INTEGER NOT NULL
        );
        CREATE INDEX IF NOT EXISTS cards_due ON cards(status, due_at);
        CREATE TABLE IF NOT EXISTS reviews (
            id TEXT PRIMARY KEY, card_id TEXT NOT NULL REFERENCES cards(id) ON DELETE CASCADE,
            rating TEXT NOT NULL CHECK(rating IN ('again', 'good')),
            reviewed_at INTEGER NOT NULL
        );
    """)
    return db


def rows(db: sqlite3.Connection, sql: str, params: tuple = ()) -> list[dict]:
    return [dict(row) for row in db.execute(sql, params)]


def state(db: sqlite3.Connection) -> dict:
    return {
        "courses": rows(db, "SELECT * FROM courses ORDER BY name"),
        "sources": rows(db, "SELECT * FROM sources ORDER BY created_at DESC, rowid DESC"),
        "cards": rows(db, "SELECT * FROM cards ORDER BY created_at DESC, rowid DESC"),
    }


def create_course(db: sqlite3.Connection, name: str) -> dict:
    if not isinstance(name, str):
        raise ValueError("Course name must be text.")
    name = name.strip()
    if not 1 <= len(name) <= 80:
        raise ValueError("Course name must be 1–80 characters.")
    item = {"id": uuid.uuid4().hex, "name": name}
    try:
        with db:
            db.execute("INSERT INTO courses(id, name) VALUES(:id, :name)", item)
    except sqlite3.IntegrityError as exc:
        raise ValueError("That course already exists.") from exc
    return item


def create_source(db: sqlite3.Connection, course_id: str | None, title: str,
                  content: str, kind: str) -> dict:
    if not isinstance(title, str) or not isinstance(content, str):
        raise ValueError("Source title and content must be text.")
    if course_id is not None and not isinstance(course_id, str):
        raise ValueError("Invalid course ID.")
    title, content = title.strip(), content.strip()
    if kind not in ("capture", "material"):
        raise ValueError("Invalid source kind.")
    if not 1 <= len(title) <= 120 or not 1 <= len(content) <= 100_000:
        raise ValueError("A title and up to 100,000 characters of text are required.")
    if course_id is not None and not db.execute(
        "SELECT 1 FROM courses WHERE id = ?", (course_id,)
    ).fetchone():
        raise ValueError("Course not found.")
    item = {"id": uuid.uuid4().hex, "course_id": course_id, "title": title,
            "content": content, "kind": kind, "created_at": int(time.time())}
    with db:
        db.execute("""INSERT INTO sources(id, course_id, title, content, kind, created_at)
                      VALUES(:id, :course_id, :title, :content, :kind, :created_at)""", item)
    return item


def delete_source(db: sqlite3.Connection, source_id: str) -> None:
    with db:
        result = db.execute("DELETE FROM sources WHERE id = ?", (source_id,))
    if result.rowcount != 1:
        raise ValueError("Source not found.")


def create_card(db: sqlite3.Connection, source_id: str, question: str,
                answer: str, quote: str) -> dict:
    if not all(isinstance(value, str) for value in (source_id, question, answer, quote)):
        raise ValueError("Card fields must be text.")
    source = db.execute("SELECT content FROM sources WHERE id = ?", (source_id,)).fetchone()
    if source is None:
        raise ValueError("Source not found.")
    question, answer, quote = question.strip(), answer.strip(), quote.strip()
    if not 1 <= len(question) <= 300 or not 1 <= len(answer) <= 300:
        raise ValueError("Question and answer must be 1–300 characters.")
    if not 1 <= len(quote) <= 1000 or quote not in source["content"] or answer not in quote:
        raise ValueError("The answer must appear in an exact quote from this source.")
    item = {"id": uuid.uuid4().hex, "source_id": source_id, "question": question,
            "answer": answer, "quote": quote, "status": "draft",
            "due_at": int(time.time()), "interval_days": 0,
            "created_at": int(time.time())}
    with db:
        db.execute("""INSERT INTO cards(id, source_id, question, answer, quote,
                      status, due_at, interval_days, created_at)
                      VALUES(:id, :source_id, :question, :answer, :quote,
                      :status, :due_at, :interval_days, :created_at)""", item)
    return item


def accept_card(db: sqlite3.Connection, card_id: str) -> None:
    with db:
        result = db.execute("UPDATE cards SET status = 'active' WHERE id = ? AND status = 'draft'",
                            (card_id,))
    if result.rowcount != 1:
        raise ValueError("Draft card not found.")


def review_card(db: sqlite3.Connection, card_id: str, rating: str,
                now: int | None = None) -> dict:
    if rating not in ("again", "good"):
        raise ValueError("Rating must be again or good.")
    now = int(time.time()) if now is None else now
    card = db.execute("SELECT * FROM cards WHERE id = ? AND status = 'active'",
                      (card_id,)).fetchone()
    if card is None or card["due_at"] > now:
        raise ValueError("Active card is not due.")
    interval = 1 if rating == "again" else (3 if card["interval_days"] == 0 else
                                               min(card["interval_days"] * 2, 30))
    due_at = now + interval * 86400
    with db:
        db.execute("UPDATE cards SET interval_days = ?, due_at = ? WHERE id = ?",
                   (interval, due_at, card_id))
        db.execute("INSERT INTO reviews(id, card_id, rating, reviewed_at) VALUES(?, ?, ?, ?)",
                   (uuid.uuid4().hex, card_id, rating, now))
    return {"due_at": due_at, "interval_days": interval}
