from models import Problem, Review
from datetime import date
from storage import initialize_database, save_problem, get_all_problems, save_review, get_all_reviews
import sqlite3
import pytest


def test_saved_problem_can_be_loaded(tmp_path):
    database_path = str(tmp_path / "test.db")
    initialize_database(database_path)

    problem = Problem(
        number=1,
        name="Two Sum",
        difficulty="Easy",
        topic="Arrays & Hashing",
        notes="Use a hashmap",
    )

    save_problem(database_path, problem)
    loaded = get_all_problems(database_path)

    assert loaded == [problem]
    
def test_saved_review_can_be_loaded(tmp_path):
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
    
    review = Review(
        problem_number=1,
        reviewed_on=date(2026, 9, 20),
        mastery_level="Solved Independently"
    )
    
    save_review(database_path, review)
    loaded = get_all_reviews(database_path)
    
    assert loaded == [review]
    
def test_review_for_missing_problem_is_rejected(tmp_path):
    database_path = str(tmp_path / "test.db")
    initialize_database(database_path)
    
    review = Review(
        problem_number=999,
        reviewed_on=date(2026, 9, 20),
        mastery_level="Solved Independently"
    )
    
    with pytest.raises(sqlite3.IntegrityError, match="FOREIGN KEY"):
        save_review(database_path, review)  