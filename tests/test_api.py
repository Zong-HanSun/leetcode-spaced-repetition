from fastapi.testclient import TestClient

import main
from models import Problem, Review
from datetime import date
from storage import initialize_database, save_problem, get_all_reviews


def test_post_review_saves_valid_attempt(tmp_path, monkeypatch):
    database_path = str(tmp_path / "test.db")
    initialize_database(database_path)

    problem = Problem(
        number=1,
        name="Two Sum",
        difficulty="Easy",
        topic="Arrays & Hashing",
        notes="",
    )
    save_problem(database_path, problem)

    monkeypatch.setattr(main, "DATABASE_PATH", database_path)

    payload = {
        "problem_number": 1,
        "reviewed_on": "2026-09-20",
        "mastery_level": "Solved Independently",
    }

    with TestClient(main.app) as client:
        response = client.post("/reviews", json=payload)

    assert response.status_code == 201
    assert response.json() == payload
    assert get_all_reviews(database_path) == [Review(problem_number=1,
                                                    reviewed_on=date(2026, 9, 20),
                                                    mastery_level="Solved Independently")]