from datetime import date

from tracker import record_review, get_latest_review


def test_record_review_appends_attempt_without_replacing_history():
    previous_review = {
        "problem_number": 1,
        "reviewed_on": date(2026, 9, 8),
        "mastery_level": "Learned Solution",
    }
    reviews = [previous_review.copy()]

    record_review(
        reviews,
        1,
        date(2026, 9, 9),
        "Solved Independently",
    )

    assert reviews == [
        previous_review,
        {
            "problem_number": 1,
            "reviewed_on": date(2026, 9, 9),
            "mastery_level": "Solved Independently",
        },
    ]

def test_get_newest_attempt_out_of_order():
    sample_review_one = {
            "problem_number": 1,
            "reviewed_on": date(2026, 9, 8),
            "mastery_level": "Learned Solution",
        }

    sample_review_two = {
            "problem_number": 1,
            "reviewed_on": date(2026, 9, 9),
            "mastery_level": "Learned Solution",
        }

    reviews = [sample_review_two, sample_review_one]
    latest_review = get_latest_review(reviews, 1)
    assert latest_review == sample_review_two
    
def test_get_correct_problem_despite_date():
    sample_review_one = {
            "problem_number": 1,
            "reviewed_on": date(2026, 9, 8),
            "mastery_level": "Learned Solution",
        }

    sample_review_two = {
            "problem_number": 2,
            "reviewed_on": date(2026, 9, 9),
            "mastery_level": "Learned Solution",
        }
    
    reviews = [sample_review_two, sample_review_one]
    latest_review = get_latest_review(reviews, 1)
    assert latest_review == sample_review_one
    
def test_no_match_return_none():
    sample_review_one = {
            "problem_number": 1,
            "reviewed_on": date(2026, 9, 8),
            "mastery_level": "Learned Solution",
        }
    
    reviews = [sample_review_one]
    
    assert get_latest_review(reviews, 67) is None
    
    
    
    
    
