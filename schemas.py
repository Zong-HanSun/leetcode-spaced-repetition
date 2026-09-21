from datetime import date

from pydantic import BaseModel, Field, field_validator

from scheduler import REVIEW_INTERVALS


class ReviewCreate(BaseModel):
    problem_number: int = Field(gt=0)
    reviewed_on: date
    mastery_level: str

    @field_validator("mastery_level")
    @classmethod
    def validate_mastery_level(cls, value: str) -> str:
        if value not in REVIEW_INTERVALS:
            raise ValueError(f"Invalid mastery level: {value}")
        return value
    