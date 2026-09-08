from datetime import date

from scheduler import calculate_next_review

import pytest


def test_independent_solve_schedules_seven_days_later():
    reviewed_on = date(2026, 9, 8)

    next_review = calculate_next_review(
        reviewed_on,
        "Solved Independently",
    )

    assert next_review == date(2026, 9, 15)
    
def test_independent_review_crosses_month_boundary():
    reviewed_on = date(2026, 9, 29)
    
    next_review = calculate_next_review(
        reviewed_on,
        "Solved Independently"
    )
    
    assert next_review == date(2026, 10, 6)

def test_unknown_mastery_level_raises_error():
    with pytest.raises(ValueError):
        calculate_next_review(date(2026, 9, 8), "Unknown")