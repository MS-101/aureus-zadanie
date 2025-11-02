from datetime import date, datetime
from sqlalchemy import String, JSON
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional

from . import BaseModel


class LoanView(BaseModel):
    __tablename__ = "loan_list"

    # loan
    loan_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    loan_number: Mapped[int]
    loan_title: Mapped[Optional[str]] = mapped_column(String(50))
    loan_description: Mapped[Optional[str]]
    loan_type_id: Mapped[Optional[int]]
    loan_type_label: Mapped[Optional[str]]
    loan_status_id: Mapped[Optional[int]]
    loan_status_label: Mapped[Optional[str]]
    owner_person_id: Mapped[int] = mapped_column(String(36))
    owner_last_name: Mapped[Optional[str]] = mapped_column(String(100))
    owner_first_name: Mapped[Optional[str]] = mapped_column(String(100))
    created_at: Mapped[datetime]
    modified_at: Mapped[Optional[datetime]]
    modified_by: Mapped[Optional[str]] = mapped_column(String(36))
    is_locked: Mapped[Optional[str]]
    notes: Mapped[str]

    # loan attributes
    guarantor_last_name: Mapped[Optional[str]]
    guarantor_first_name: Mapped[Optional[str]]
    assessor_last_name: Mapped[Optional[str]]
    assessor_first_name: Mapped[Optional[str]]
    loan_amount: Mapped[Optional[float]]
    currency: Mapped[Optional[str]]
    due_date: Mapped[Optional[datetime]]

    # loan principal views
    principal_balance: Mapped[Optional[float]]
    overdue_amount: Mapped[Optional[float]]
