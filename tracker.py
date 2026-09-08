from datetime import date


def get_latest_review(reviews: list, problem_number: int) -> dict | None:
    latest_review = None

    for review in reviews:
        if review["problem_number"] == problem_number:
            if (
                latest_review is None
                or review["reviewed_on"] > latest_review["reviewed_on"]
            ):
                latest_review = review

    return latest_review


def record_review(
    reviews: list,
    problem_number: int,
    reviewed_on: date,
    mastery_level: str,
) -> None:
    review = {
        "problem_number": problem_number,
        "reviewed_on": reviewed_on,
        "mastery_level": mastery_level,
    }

    reviews.append(review)