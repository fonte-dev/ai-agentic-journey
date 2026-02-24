# Day 33 - Strict Types
# Task: Try passing a string to an int field. Watch Pydantic coerce or fail.
# Learning goal: See the difference between normal (coercion) and strict validation
# Date: Feb 2026
# Status: DONE ✅


from pydantic import BaseModel, ValidationError, ConfigDict
from typing import Literal, Any


# Normal model (default behavior = tries to fix/coerce data)
class PatientIntakeNormal(BaseModel):
    patient_id: int
    first_name: str
    age: int
    risk_level: Literal["low", "medium", "high"] = "low"


# Strict model (fails fast on wrong types)
class PatientIntakeStrict(BaseModel):
    model_config = ConfigDict(strict=True)  # ← Makes the whole model strict

    patient_id: int
    first_name: str
    age: int
    risk_level: Literal["low", "medium", "high"] = "low"


if __name__ == "__main__":
    test_data: dict[str, Any] = {
        "patient_id": "999",  # string instead of int
        "first_name": "Juan",
        "age": "35",  # string instead of int
        "risk_level": "high",
    }

    print("Normal Model (coercion)\n")
    try:
        patient = PatientIntakeNormal(**test_data)
        print("Normal model succeeded (it coerced strings to int):")
        print(patient)
    except ValidationError as e:
        print("Normal model failed:", e)

    print("\nStrict Model (no coercion)\n")
    try:
        patient = PatientIntakeStrict(**test_data)
        print("Strict model succeeded (surprisingly):")
        print(patient)
    except ValidationError as e:
        print("Strict model failed (as expected):")
        for error in e.errors():
            print(f"  → Field {error['loc']}: {error['msg']}")
