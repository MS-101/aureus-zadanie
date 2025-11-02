from datetime import datetime
from pydantic import BaseModel
from typing import Optional

from src.models import LoanView


class LoanDto(BaseModel):
    loan_id: Optional[str] = None
    loan_number: Optional[int] = None
    loan_title: Optional[str] = None
    loan_type_id: Optional[int] = None
    loan_type_label: Optional[str] = None
    loan_status_id: Optional[int] = None
    loan_status_label: Optional[str] = None
    loan_owner_last_name: Optional[str] = None
    loan_owner_first_name: Optional[str] = None
    referent_last_name: Optional[str] = None
    referent_first_name: Optional[str] = None
    guarantor_last_name: Optional[str] = None
    guarantor_first_name: Optional[str] = None    
    loan_number: Optional[float] = None
    loan_amount_unpaid: Optional[float] = None
    overdue_amount: Optional[float] = None
    loan_currency: Optional[str] = None
    loan_due_date: Optional[datetime] = None
    created_at: Optional[datetime] = None

    model_config = {
        "json_schema_extra": {
            "example": {
                "loan_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "loan_number": 123,
                "loan_title": "[#123] Stabilizačná pôžička",
                "loan_type_id": 1,
                "loan_type_label": "Stabilizačná pôžička",
                "loan_status_id": 1,
                "loan_status_label": "Nová",
                "loan_owner_last_name": "Mrkvička",
                "loan_owner_first_name": "Jozef",
                "referent_last_name": "Zelená",
                "referent_first_name": "Anna",
                "guarantor_last_name": "Modrý",
                "guarantor_first_name": "Adam",
                "loan_amount": 4000,
                "loan_amount_unpaid": 3589.37,
                "overdue_amount": 123.45,
                "loan_currency": "EUR",
                "loan_due_date": "2030-12-31T23:59:59.999Z",
                "created_at": "2023-01-01T14:15:16.789Z"
            }
        }
    }

    @classmethod
    def from_view(cls, loan_view: LoanView):
        return cls(
            loan_id=loan_view.loan_id,
            loan_number=loan_view.loan_number,
            loan_title=loan_view.loan_title,
            loan_type_id=loan_view.loan_type_id,
            loan_type_label=loan_view.loan_type_label,
            loan_status_id=loan_view.loan_status_id,
            loan_status_label=loan_view.loan_status_label,
            loan_owner_last_name=loan_view.owner_last_name,
            loan_owner_first_name=loan_view.owner_first_name,
            referent_last_name=loan_view.assessor_last_name,
            referent_first_name=loan_view.assessor_first_name,
            guarantor_last_name=loan_view.guarantor_last_name,
            guarantor_first_name=loan_view.guarantor_first_name,
            loan_amount_unpaid=loan_view.principal_balance,
            overdue_amount=loan_view.overdue_amount,
            loan_currency=loan_view.currency,
            loan_due_date=loan_view.due_date,
            created_at=loan_view.created_at
        )