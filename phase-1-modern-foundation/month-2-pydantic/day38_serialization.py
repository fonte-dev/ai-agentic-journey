# Day 38 - Serialization
# Task: model.model_dump() and model_dump_json().
# Learning goal: Preparing data for API transmission.
# Date: Feb 2026
# Status: DONE ✅


from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class Address(BaseModel):
    street: str = Field(..., description="Full street address")
    city: str = Field(..., description="City or town")
    zip_code: str = Field(..., description="Postal code")
    country: str = Field("Argentina", description="Country")


class PatientIntake(BaseModel):
    patient_id: int = Field(..., description="Patient ID")
    first_name: str = Field(..., description="First name")
    last_name: str = Field(..., description="Last name")
    age: int = Field(..., description="Age")
    address: Address
    emergency_contact: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.now)


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
        },
    }

    patient = PatientIntake(**data)

    print("1. As Python dict:")
    print(patient.model_dump())

    print("\n2. As pretty JSON string:")
    print(patient.model_dump_json(indent=2))

    print("\n3. As dict excluding created_at:")
    print(patient.model_dump(exclude={"created_at"}))

    print(patient.model_dump(exclude_none=True))
