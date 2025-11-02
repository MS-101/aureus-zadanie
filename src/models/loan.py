from datetime import date, datetime
from sqlalchemy import String, JSON
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional

from . import BaseModel


class Loan(BaseModel):
    __tablename__ = "loan"

    loan_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    loan_number: Mapped[int]
    loan_title: Mapped[Optional[str]] = mapped_column(String(50))
    loan_description: Mapped[Optional[str]]
    loan_type_id: Mapped[Optional[int]]
    loan_status_id: Mapped[Optional[int]]
    owner_person_id: Mapped[int] = mapped_column(String(36))
    created_at: Mapped[datetime]
    modified_at: Mapped[Optional[datetime]]
    modified_by: Mapped[Optional[str]] = mapped_column(String(36))
    is_locked: Mapped[Optional[str]]
    notes: Mapped[str]
