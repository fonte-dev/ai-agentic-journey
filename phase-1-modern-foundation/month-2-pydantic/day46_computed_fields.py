# Day 46 - Computed Fields
# Task: @computed_field. Calculate bmi from height and weight automatically.
# Learning goal: Automating derived data.
# Date: Feb 2026
# Status: DONE ✅

from pydantic import BaseModel, computed_field, Field


class PatientHealth(BaseModel):
    """Patient health data with automatic BMI calculation."""

    patient_id: int
    height_cm: float = Field(..., gt=50, le=250, description="Height in centimeters")
    weight_kg: float = Field(..., gt=2, le=300, description="Weight in kilograms")

    @computed_field
    def bmi(self) -> float:
        return round(self.weight_kg / (self.height_cm / 100) ** 2, 2)


if __name__ == "__main__":
    patient = PatientHealth(patient_id=101, height_cm=170, weight_kg=68)

    print("Patient data:")
    print(patient.model_dump_json(indent=2))

    print(f"\nBMI: {patient.bmi}")
