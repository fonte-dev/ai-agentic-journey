# Day 47 - Immutability
# Task: ConfigDict(frozen=True).
# Learning goal: Creating "Read-Only" records (Clinical integrity).
# Date: Feb 2026
# Status: DONE ✅


from pydantic import BaseModel, ConfigDict, Field, ValidationError
from datetime import datetime


class SessionNote(BaseModel):
    """Therapy session note that should never be modified after creation."""

    patient_id: int = Field(..., description="Patient ID")
    subjective: str
    objective: str
    plan: str
    created_at: datetime = Field(default_factory=datetime.now)

    model_config = ConfigDict(frozen=True)


if __name__ == "__main__":
    note = SessionNote(
        patient_id=101,
        subjective="El paciente reportó mucha ansiedad",
        objective="Se presentó agitado",
        plan="Técnicas de respiración + seguimiento",
    )

    print("SessionNote created:")
    print(note.model_dump_json(indent=2))

    print("\nTrying to modify the note...")
    try:
        note.subjective = "Cambio malicioso"
    except Exception as e:
        print(f"Modification blocked: {type(e).__name__} - {e}")
