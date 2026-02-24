# Day 45 - Generic Models
# Task: Create a Response wrapper model.
# Learning goal: Advanced abstraction.
# Date: Feb 2026
# Status: DONE ✅

from pydantic import BaseModel
from typing import Generic, TypeVar, List, Optional

# This is the magic variable that makes the model generic
T = TypeVar("T")


class ApiResponse(BaseModel, Generic[T]):
    """Reusable response wrapper for any type of data."""

    success: bool
    data: T  # This will be replaced by PatientIntake, list[...], etc.
    message: Optional[str] = None
    error: Optional[str] = None


# Reuse models from previous days
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


if __name__ == "__main__":
    # Sample data
    patient = PatientIntake(
        patient_id=101,
        first_name="Luna",
        last_name="Martínez",
        age=25,
        address=Address(
            street="Av. Rivadavia 4567", city="Villa Sarmiento", zip_code="1708"
        ),
    )

    # Example 1: Response containing ONE PatientIntake
    response_single = ApiResponse[PatientIntake](
        success=True, data=patient, message="Patient intake saved successfully"
    )

    # Example 2: Response containing a LIST of PatientIntake
    response_list = ApiResponse[List[PatientIntake]](
        success=True,
        data=[patient, patient],  # two patients in a list
        message="Patients retrieved",
    )

    print("Single Patient Response")
    print(response_single.model_dump_json(indent=2))

    print("\nList of Patients Response")
    print(response_list.model_dump_json(indent=2))
