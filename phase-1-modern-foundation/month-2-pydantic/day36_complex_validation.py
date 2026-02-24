# Day 36 - Complex Validation
# Task: Validator that checks 2 fields (e.g., if under_18, ensure parent_contact exists).
# Learning goal: Contextual Logic: Dependencies between data points.
# Date: Feb 2026
# Status: DONE ✅

from pydantic import BaseModel, field_validator, model_validator, ValidationError
from typing import Optional, Literal


class PatientIntake(BaseModel):
    """Real intake form for MERITUM with complex rules."""

    patient_id: int
    first_name: str
    last_name: str
    age: int
    risk_level: Literal["low", "medium", "high"] = "low"
    parent_contact: Optional[str] = None  # Only required if age < 18
    emergency_contact: Optional[str] = None  # Only required if risk_level == "high"

    @field_validator("age")
    @classmethod
    def age_must_be_positive(cls, v: int) -> int:
        if v <= 0:
            raise ValueError("Age must be greater than zero")
        return v

    @model_validator(mode="after")
    def check_age_and_risk_requirements(self):
        if self.age < 18 and self.parent_contact is None:
            raise ValueError("Patient is under 18. Parent contact is required.")

        if self.risk_level == "high" and self.emergency_contact is None:
            raise ValueError("High risk patient. Emergency contact is required.")

        return self


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
        # Bad case 1: Under 18 without parent_contact
        {
            "patient_id": 102,
            "first_name": "Mateo",
            "last_name": "García",
            "age": 14,
            "risk_level": "low",
        },
        # Bad case 2: High risk without emergency_contact
        {
            "patient_id": 103,
            "first_name": "Sofía",
            "last_name": "López",
            "age": 32,
            "risk_level": "high",
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
