# Day 39 - Custom Types
# Task: Use EmailStr, HttpUrl from Pydantic.
# Learning goal: Leveraging built-in validation tools.
# Date: Feb 2026
# Status: DONE ✅

from pydantic import BaseModel, EmailStr, HttpUrl, ValidationError
from typing import Optional
from typing import Any


class ContactInfo(BaseModel):
    """Contact information for MERITUM (used by families and ATs)."""

    full_name: str
    email: EmailStr
    phone: Optional[str] = None
    website: Optional[HttpUrl] = None


if __name__ == "__main__":
    # Good data
    good: dict[str, Any] = {
        "full_name": "Juan Pablo Fonte",
        "email": "juan@example.com",
        "phone": "11-1234-5678",
        "website": "https://meritum.ar",
    }

    # Bad data
    bad: dict[str, Any] = {
        "full_name": "Mateo García",
        "email": "mateo@invalid-email",  # missing domain
        "website": "not-a-url",
    }

    print("\n--- Testing good data ---")
    try:
        contact = ContactInfo(**good)
        print("Good data accepted:")
        print(contact.model_dump_json(indent=2))
    except ValidationError as e:
        print("Good data failed (should not happen)")

    print("\n--- Testing bad data ---")
    try:
        ContactInfo(**bad)
    except ValidationError as e:
        print("Bad data correctly rejected:")
        for error in e.errors():
            print(f"   → {error['loc']}: {error['msg']}")
