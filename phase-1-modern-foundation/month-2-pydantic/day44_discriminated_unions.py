# Day 44 - Discriminated Unions
# Task: Handle different types of events (Message, Image, SystemLog) in one list.
# Learning goal: Polymorphism (handling diverse inputs).
# Date: Feb 2026
# Status: DONE ✅


from pydantic import BaseModel, HttpUrl
from typing import Literal, Union, Optional


# Different event types in MERITUM
class MessageEvent(BaseModel):
    type: Literal["message"] = "message"
    text: str
    from_entity: Literal["family", "at", "os"]


class RatingEvent(BaseModel):
    type: Literal["rating"] = "rating"
    from_entity: Literal["family", "at", "os"]
    to_entity: Literal["family", "at", "os"]
    score: int
    comment: Optional[str] = None


class SystemLogEvent(BaseModel):
    type: Literal["system_log"] = "system_log"
    message: str


class ImageEvent(BaseModel):
    type: Literal["image"] = "image"
    image_url: HttpUrl
    caption: Optional[str] = None


class SessionNoteEvent(BaseModel):
    type: Literal["session_note"] = "session_note"
    note: str


# Discriminated Union - Pydantic uses the "type" field to choose the right model
Event = Union[MessageEvent, RatingEvent, SystemLogEvent, ImageEvent, SessionNoteEvent]


class ActivityLog(BaseModel):
    """A log of mixed events in MERITUM."""

    events: list[Event]


if __name__ == "__main__":
    log_data = {
        "events": [
            {
                "type": "message",
                "text": "Hola, ¿cómo está mi hijo hoy?",
                "from_entity": "family",
            },
            {
                "type": "rating",
                "from_entity": "family",
                "to_entity": "at",
                "score": 5,
                "comment": "Excelente atención",
            },
            {
                "type": "system_log",
                "message": "Payment processed successfully",
            },
            {
                "type": "image",
                "image_url": "https://meritum.ar/uploads/session-105.jpg",
                "caption": "Foto de la sesión de hoy",
            },
        ]
    }

    log = ActivityLog.model_validate(log_data)
    print("ActivityLog parsed successfully!")
    print(log.model_dump_json(indent=2))
