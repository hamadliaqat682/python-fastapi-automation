from typing import Literal
from pydantic import BaseModel, EmailStr, Field, field_validator

class Lead(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    email: EmailStr
    company: str = Field(min_length=2, max_length=150)
    phone: str | None = None
    employees: int = Field(ge=0, le=1000000)
    interested_in: Literal["automation", "ai-agent", "crm", "other"]
    notes: str = Field(default="", max_length=2000)

    @field_validator("name", "company")
    @classmethod
    def strip_required(cls, value: str) -> str:
        value = value.strip()
        if len(value) < 2:
            raise ValueError("Must contain at least two characters")
        return value

class ProcessedLead(BaseModel):
    name: str
    email: EmailStr
    company: str
    phone: str | None
    score: int
    priority: Literal["high", "medium", "low"]
    tags: list[str]
    crm_payload: dict
