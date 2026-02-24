# Day 42 - JSON Parsing
# Task: Read a complex JSON file into a Pydantic model.
# Learning goal: Ingesting external data.
# Date: Feb 2026
# Status: DONE ✅


from pydantic import BaseModel, ValidationError
from typing import Literal


class Address(BaseModel):
    street: str
    city: str
    zip_code: str


class PatientIntake(BaseModel):
    patient_id: int
    first_name: str
    last_name: str
    age: int
    address: Address
    risk_level: Literal["low", "medium", "high"] = "low"


if __name__ == "__main__":
    json_data = """
    {
        "patient_id": 105,
        "first_name": "Camila",
        "last_name": "Rodríguez",
        "age": 29,
        "address": {
            "street": "Calle 7 de Julio 234",
            "city": "Villa Sarmiento",
            "zip_code": "1708"
        },
        "risk_level": "medium"
    }
    """

    try:
        patient = PatientIntake.model_validate_json(json_data)
        print("Successfully parsed JSON into Pydantic model:")
        print(patient.model_dump_json(indent=2))
    except ValidationError as e:
        print("Failed to parse JSON:")
        for error in e.errors():
            print(f"   → {error['loc']}: {error['msg']}")

    bad_json = """
    {
        "patient_id": 105,
        "first_name": "Camila",
        "last_name": "Rodríguez",
        "age": "AB",
        "address": {
            "street": "Calle 7 de Julio 234",
            "city": "Villa Sarmiento",
            "zip_code": "1708"
        }
    }
    """

    try:
        PatientIntake.model_validate_json(bad_json)
    except ValidationError as e:
        print("\nBad data correctly rejected:")
        for error in e.errors():
            print(f"   → {error['loc']}: {error['msg']}")
