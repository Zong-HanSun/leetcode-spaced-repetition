from datetime import date, timedelta

REVIEW_INTERVALS = {
    "Learned Solution": 1,
    "Partial Recall": 2,
    "Solved with Struggle": 3,
    "Solved Independently": 7,
    "Mastered": 14,
}

def calculate_next_review(reviewed_on: date, mastery_level: str) -> date:
    if mastery_level not in REVIEW_INTERVALS:
        raise ValueError(f"Invalid mastery level: {mastery_level}")

    days = REVIEW_INTERVALS[mastery_level]
    return reviewed_on + timedelta(days=days)
