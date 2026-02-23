# Day 31 - Type Hinting
# Task: Read Python typing docs (List, Dict, Optional, Union).
# Learning goal: Precision in language.
# Date: Feb 2026
# Status: Done ✅

from typing import List, Optional, Literal
from dataclasses import dataclass
from datetime import datetime


@dataclass
class SessionNote:
    """One therapy session note (will be used by the LLM later)."""

    subjective: str
    objective: str
    assessment: str
    plan: str
    patient_id: int
    at_id: int
    date: datetime
    duration_minutes: int
    tags: Optional[List[str]] = None


@dataclass
class Rating:
    """Rating between the three sides of MERITUM."""

    from_entity: Literal["family", "at", "os"]
    to_entity: Literal["family", "at", "os"]
    score: Literal[1, 2, 3, 4, 5]
    date: datetime
    comment: Optional[str] = None


def filter_severity_notes(notes: List[SessionNote]) -> List[SessionNote]:
    """Return only SessionNotes that contain at least one severity tag."""
    severity_tags = {"crisis", "suicide_risk", "severe", "emergency", "high_risk"}

    return [
        note
        for note in notes
        if note.tags and any(tag.lower() in severity_tags for tag in note.tags)
    ]


if __name__ == "__main__":
    s1 = SessionNote(
        subjective="Patient reports anxiety",
        objective="Appears agitated",
        assessment="Moderate crisis",
        plan="Follow-up in 48h",
        patient_id=101,
        at_id=5,
        date=datetime(2026, 2, 22, 14, 30),
        duration_minutes=45,
        tags=["crisis", "anxiety"],
    )

    s2 = SessionNote(
        subjective="Feeling good today",
        objective="Calm and talkative",
        assessment="Stable",
        plan="Continue treatment",
        patient_id=102,
        at_id=5,
        date=datetime(2026, 2, 22, 15, 0),
        duration_minutes=30,
        tags=None,
    )

    s3 = SessionNote(
        subjective="Suicidal thoughts",
        objective="Withdrawn",
        assessment="High risk",
        plan="Immediate referral",
        patient_id=103,
        at_id=5,
        date=datetime(2026, 2, 22, 16, 0),
        duration_minutes=60,
        tags=["suicide_risk", "emergency"],
    )

    notes = [s1, s2, s3]
    filtered = filter_severity_notes(notes)

    print(f"Total notes: {len(notes)}")
    print(f"Severity notes found: {len(filtered)}")
    for note in filtered:
        print(f"→ Patient {note.patient_id} | Tags: {note.tags}")
