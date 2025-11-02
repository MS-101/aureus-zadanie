from datetime import date, datetime
from sqlalchemy import String, JSON
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional

from . import BaseModel


class NaturalPerson(BaseModel):
    __tablename__ = "natural_person"

    person_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    personal_identification_number: Mapped[str] = mapped_column(String(10))
    first_name: Mapped[Optional[str]] = mapped_column(String(100))
    last_name: Mapped[Optional[str]] = mapped_column(String(100))
    title_before: Mapped[Optional[str]] = mapped_column(String(15))
    date_of_birth: Mapped[date]
    nationality: Mapped[str]
    address: Mapped[str]
    correspondence_address: Mapped[Optional[str]]
    email: Mapped[Optional[str]]
    phone_number: Mapped[Optional[str]]
    created_at: Mapped[Optional[datetime]]
    last_modified: Mapped[Optional[datetime]]
    preference: Mapped[dict] = mapped_column(JSON)
    is_service_account: Mapped[bool]
    title_after: Mapped[Optional[str]] = mapped_column(String(15))
