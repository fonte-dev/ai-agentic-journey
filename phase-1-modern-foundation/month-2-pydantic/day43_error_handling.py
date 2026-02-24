# Day 43 - Error Handling
# Task: Catch ValidationError. Print readable error messages for users.
# Learning goal: UX: Translating technical errors into human guidance.
# Date: Feb 2026
# Status: DONE ✅


from pydantic import BaseModel, Field, ValidationError
from typing import Optional, Literal


class PatientIntake(BaseModel):
    """Real intake form for MERITUM."""

    patient_id: int = Field(..., description="Patient ID")
    first_name: str = Field(..., min_length=2)
    last_name: str = Field(..., min_length=2)
    age: int = Field(..., gt=0)
    risk_level: Literal["low", "medium", "high"] = "low"
    parent_contact: Optional[str] = None


if __name__ == "__main__":
    test_cases = [
        {"patient_id": 101, "first_name": "Luna", "last_name": "Martínez", "age": 25},
        {"patient_id": 102, "first_name": "Mateo", "age": 14},  # missing last_name
        {
            "patient_id": 103,
            "first_name": "Sofía",
            "last_name": "López",
            "age": -5,
        },  # negative age
        {
            "patient_id": 104,
            "first_name": "A",
            "last_name": "García",
            "age": 30,
        },  # name too short
    ]

    for i, data in enumerate(test_cases, 1):
        print(f"\n--- Test {i} ---")
        try:
            patient = PatientIntake(**data)
            print(f"VALID: {patient.first_name} {patient.last_name}")
        except ValidationError as e:
            print("RECHAZADO — Por favor solucione estos problemas:")
            for error in e.errors():
                field = error["loc"][-1]
                msg = error["msg"]

                # Human-friendly messages
                if field == "age" and "greater_than" in error["type"]:
                    print(f"   → Edad: Debe ser mayor a 0 años")
                elif "too_short" in error["type"]:
                    if field == "first_name":
                        print(f"   → Nombre: Debe tener al menos 2 letras")
                    else:
                        print(f"   → {field}: Debe tener al menos 2 letras")
                elif "missing" in error["type"]:
                    if field == "last_name":
                        print(f"   → Apellido: Este campo es obligatorio")
                    else:
                        print(f"   → {field}: Este campo es obligatorio")
                else:
                    print(f"   → {field}: {msg}")
