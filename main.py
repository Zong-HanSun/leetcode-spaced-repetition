from pathlib import Path

from fastapi import FastAPI

from models import Problem, Review
from storage import get_all_problems, get_all_reviews
from datetime import date
from tracker import get_due_problems

app = FastAPI()

DATABASE_PATH = str(Path(__file__).resolve().parent / "tracker.db")


@app.get("/problems", response_model=list[Problem])
def list_problems() -> list[Problem]:
    return get_all_problems(DATABASE_PATH)


@app.get("/reviews", response_model=list[Review])
def list_reviews() -> list[Review]:
    return get_all_reviews(DATABASE_PATH)


@app.get("/problems/due", response_model=list[Problem])
def list_due_problems() -> list[Problem]:
    problems = list_problems()
    reviews = list_reviews()

    list_due_problems = get_due_problems(problems, reviews, date.today())
    return list_due_problems
