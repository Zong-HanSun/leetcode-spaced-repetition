from datetime import date, timedelta

REVIEW_INTERVALS = {
    "Learned solution": 1,
    "Partial recall": 2,
    "Solved with struggle": 3,
    "Solved independently": 7,
    "Mastered": 14,
}

def calculate_next_review(reviewed_on: date, mastery_level: str) -> date:
    if mastery_level not in REVIEW_INTERVALS:
        raise ValueError(f"Invalid mastery level: {mastery_level}")

    days = REVIEW_INTERVALS[mastery_level]
    return reviewed_on + timedelta(days=days)

assert calculate_next_review(
    date(2026, 9, 8), "Learned solution"
) == date(2026, 9, 9)

assert calculate_next_review(
    date(2026, 9, 8), "Partial recall"
) == date(2026, 9, 10)

assert calculate_next_review(
    date(2026, 9, 8), "Solved with struggle"
) == date(2026, 9, 11)

assert calculate_next_review(
    date(2026, 9, 8), "Solved independently"
) == date(2026, 9, 15)

assert calculate_next_review(
    date(2026, 9, 8), "Mastered"
) == date(2026, 9, 22)

assert calculate_next_review(
    date(2026, 9, 28), "Solved independently"
) == date(2026, 10, 5)

print("All scheduling checks passed.")