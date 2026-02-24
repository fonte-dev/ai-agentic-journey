# Day 35 - Validation Logic
# Task: Use @field_validator. Ensure age > 0.
# Learning goal: Clinical Logic: Implementing "Reality Testing" in code.
# Date: Feb 2026
# Status: DONE ✅

from pydantic import BaseModel, field_validator, ValidationError
from typing import Optional, Literal


class PatientIntake(BaseModel):
    """Real intake form for MERITUM."""

    patient_id: int
    first_name: str
    last_name: str
    age: int
    risk_level: Literal["low", "medium", "high"] = "low"
    parent_contact: Optional[str] = None
    emergency_contact: Optional[str] = None

    # ── Single-field validator (simple rule) ──
    @field_validator("age")
    @classmethod
    def age_must_be_positive(cls, v: int) -> int:
        if v <= 0:
            raise ValueError("Age must be greater than zero")
        return v


if __name__ == "__main__":
    test_cases = [
        # Good case
        {
            "patient_id": 101,
            "first_name": "Luna",
            "last_name": "Martínez",
            "age": 25,
            "risk_level": "medium",
        },
        # Bad case - Negative Age
        {
            "patient_id": -1,
            "first_name": "Mateo",
            "last_name": "García",
            "age": 14,
            "risk_level": "low",
        },
    ]

    for i, data in enumerate(test_cases, 1):
        print(f"\n--- Test {i} ---")
        try:
            patient = PatientIntake(**data)
            print(
                f"VALID: {patient.first_name} {patient.last_name} (age {patient.age})"
            )
        except ValidationError as e:
            print(f"REJECTED: {data.get('first_name')} {data.get('last_name')}")
            for error in e.errors():
                print(f"   → {error['msg']}")
