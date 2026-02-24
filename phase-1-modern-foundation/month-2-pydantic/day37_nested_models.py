# Day 37 - Nested Models
# Task: Create Address model, put it inside User.
# Learning goal: Handling hierarchical data (Case History).
# Date: Feb 2026
# Status: DONE ✅

from pydantic import BaseModel, Field
from typing import Optional


class Address(BaseModel):
    street: str = Field(..., description="Full street address")
    city: str = Field(..., description="City or town")
    zip_code: str = Field(..., description="Postal code")
    country: str = Field("Argentina", description="Country")


class PatientIntake(BaseModel):
    """Real intake form for MERITUM with nested address."""

    patient_id: int = Field(..., description="Patient ID")
    first_name: str = Field(..., description="First name of the patient")
    last_name: str = Field(..., description="Last name of the patient")
    age: int = Field(..., description="Age of the patient")
    address: Address  # ← Nested model
    emergency_contact: Optional[str] = None


if __name__ == "__main__":
    data = {
        "patient_id": 101,
        "first_name": "Luna",
        "last_name": "Martínez",
        "age": 25,
        "address": {
            "street": "Av. Rivadavia 4567",
            "city": "Villa Sarmiento",
            "zip_code": "1708",
            "country": "Argentina",
        },
    }

    patient = PatientIntake(**data)

    print("VALID Patient Intake created:")
    print(patient.model_dump_json(indent=2))

    print("\nAccessing nested data:")
    print(f"City: {patient.address.city}")
    print(f"Full address: {patient.address.street}, {patient.address.city}")
