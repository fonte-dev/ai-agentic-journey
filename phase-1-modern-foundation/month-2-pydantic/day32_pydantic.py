# Day 32 - Pydantic Basics
# Task: Install pydantic. Create a User model. Validate a dict.
# Learning goal: The "Intake Form" concept.
# Date: Feb 2026
# Status: DONE ✅

from pydantic import BaseModel, EmailStr, Field, ValidationError
from typing import Optional, Literal
from datetime import datetime


class PatientIntake(BaseModel):
    """This represents a real intake form for MERITUM (what families or ATs will send)."""

    patient_id: int
    first_name: str = Field(..., min_length=2, max_length=50)  # ... means required
    last_name: str = Field(..., min_length=2, max_length=50)
    age: int = Field(..., gt=0, le=120)  # gt = greater than, le = less or equal
    email: Optional[EmailStr] = None  # EmailStr auto-validates email format
    risk_level: Literal["low", "medium", "high"] = "low"  # Only these 3 values allowed
    intake_date: datetime = Field(
        default_factory=datetime.now
    )  # Auto-set to now if missing


if __name__ == "__main__":
    print("Testing good data\n")

    good_data = {
        "patient_id": 105,
        "first_name": "María",
        "last_name": "González",
        "age": 34,
        "email": "maria.gonzalez@email.com",
        "risk_level": "medium",
    }

    try:
        patient = PatientIntake(**good_data)
        print("SUCCESS:")
        print(patient.model_dump_json(indent=2))  # nice JSON output
    except ValidationError as e:
        print("Failed:", e)

    print("\nTesting bad data\n")

    bad_data = {
        "patient_id": 106,
        "first_name": "A",  # too short
        "last_name": "Lopez",
        "age": -5,  # negative age
        "email": "not-an-email",
    }

    try:
        PatientIntake(**bad_data)
    except ValidationError as e:
        print("Validation errors:")
        for error in e.errors():
            print(f"→ {error['loc']}: {error['msg']}")
