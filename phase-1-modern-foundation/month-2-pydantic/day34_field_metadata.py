# Day 34 - Field Metadata
# Task: Use Field(..., description="...").
# Learning goal: Documenting the schema for the AI (later use).
# Date: Feb 2026
# Status: DONE ✅

from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional
from datetime import datetime


class SessionNote(BaseModel):
    """A therapy session note for MERITUM."""

    model_config = ConfigDict(strict=True)

    patient_id: int = Field(..., description="Unique ID of the patient")
    at_id: int = Field(
        ..., description="ID of the Acompañante Terapéutico who wrote this note"
    )
    subjective: str = Field(
        ..., min_length=10, description="What the patient told you (in their own words)"
    )
    objective: str = Field(..., description="What you observed during the session")
    assessment: str = Field(..., description="Your professional assessment")
    plan: str = Field(..., description="What will happen next")
    duration_minutes: int = Field(
        ..., gt=0, le=120, description="How long the session lasted"
    )
    tags: Optional[List[str]] = Field(
        default=None, description="Any special tags like crisis, suicide_risk, etc."
    )
    created_at: datetime = Field(default_factory=datetime.now)


if __name__ == "__main__":
    note = SessionNote(
        patient_id=101,
        at_id=5,
        subjective="El paciente reportó mucha ansiedad por e l trabajo y problemas con la familia.",
        objective="Se presentó agitado, con sudoración y voz temblorosa.",
        assessment="Ansiedad moderada con riesgo de escalada.",
        plan="Técnicas de respiración + seguimiento en 48 horas.",
        duration_minutes=50,
        tags=["crisis", "work_stress"],
    )

    print("Valid SessionNote created:")
    print(note.model_dump_json(indent=2))

    print("\nFull JSON Schema (this is what the LLM will see):")
    import json

    print(json.dumps(note.model_json_schema(), indent=2))
