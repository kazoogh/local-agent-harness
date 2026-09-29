import tempfile
import unittest
import json
from pathlib import Path
from unittest.mock import patch

from study_assistant import ai, store


class StudyStoreTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.db = store.connect(Path(self.temp.name) / "study.sqlite3")

    def tearDown(self):
        self.db.close()
        self.temp.cleanup()

    def test_capture_to_review_and_source_deletion(self):
        course = store.create_course(self.db, "Biology")
        source = store.create_source(self.db, course["id"], "Lecture 1",
                                     "Photosynthesis converts light energy into chemical energy.",
                                     "material")
        card = store.create_card(self.db, source["id"],
                                 "What energy does photosynthesis convert?",
                                 "light energy", source["content"])
        store.accept_card(self.db, card["id"])
        reviewed = store.review_card(self.db, card["id"], "good", now=card["due_at"])
        self.assertEqual(reviewed["interval_days"], 3)
        self.assertEqual(reviewed["due_at"], card["due_at"] + 3 * 86400)
        self.assertEqual(len(store.rows(self.db, "SELECT * FROM reviews")), 1)
        store.delete_source(self.db, source["id"])
        self.assertEqual(store.rows(self.db, "SELECT * FROM cards"), [])
        self.assertEqual(store.rows(self.db, "SELECT * FROM reviews"), [])

    def test_card_must_be_supported_by_selected_source(self):
        source = store.create_source(self.db, None, "Note", "Mitosis has four stages.", "capture")
        with self.assertRaisesRegex(ValueError, "exact quote"):
            store.create_card(self.db, source["id"], "How many stages?", "five",
                              source["content"])
        with self.assertRaisesRegex(ValueError, "exact quote"):
            store.create_card(self.db, source["id"], "How many stages?", "four",
                              "Another source says four.")

    def test_invalid_course_and_early_review_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "Course not found"):
            store.create_source(self.db, "missing", "Title", "Content", "capture")
        source = store.create_source(self.db, None, "Note", "A is B.", "capture")
        card = store.create_card(self.db, source["id"], "What is A?", "B", "A is B.")
        store.accept_card(self.db, card["id"])
        with self.assertRaisesRegex(ValueError, "not due"):
            store.review_card(self.db, card["id"], "good", now=card["due_at"] - 1)


class AiValidationTests(unittest.TestCase):
    def test_only_exact_source_quotes_survive(self):
        source = "Mitosis creates two daughter cells."
        cards = ai.validate_candidates({"cards": [
            {"question": "How many daughter cells?", "answer": "two",
             "quote": source},
            {"question": "How many daughter cells?", "answer": "three",
             "quote": source},
        ]}, source)
        self.assertEqual(len(cards), 1)
        self.assertEqual(cards[0]["answer"], "two")

    def test_unsupported_model_output_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "No draft"):
            ai.validate_candidates({"cards": [
                {"question": "What is it?", "answer": "Wrong", "quote": "Fabricated quote"}
            ]}, "Real source")

    def test_local_model_request_uses_selected_source_and_validates_response(self):
        class Response:
            status = 200

            def __enter__(self):
                return self

            def __exit__(self, *_):
                return False

            def read(self, *_):
                return json.dumps({"response": json.dumps({"cards": [
                    {"question": "What does A become?", "answer": "B", "quote": "A becomes B."}
                ]})}).encode()

        class Opener:
            def open(self, request, timeout):
                self.payload = json.loads(request.data)
                return Response()

        opener = Opener()
        with patch("study_assistant.ai.urllib.request.build_opener", return_value=opener):
            cards = ai.draft_cards("A becomes B.", "test-model",
                                   "http://127.0.0.1:11434/api/generate")
        self.assertEqual(cards[0]["answer"], "B")
        self.assertIn("A becomes B.", opener.payload["prompt"])
        self.assertEqual(opener.payload["model"], "test-model")
        with self.assertRaisesRegex(ValueError, "local HTTP"):
            ai.draft_cards("A becomes B.", "test-model", "https://example.com/api")


if __name__ == "__main__":
    unittest.main()
