# users.py
from fastapi import APIRouter, HTTPException
from sqlalchemy import select, and_, or_
from typing import Optional

from src.dependencies import NaturalPersonDependency
from src.dtos import LoanDto
from src.models import LoanView


loan_router = APIRouter(tags=["Loan"])

@loan_router.get("/loans", description="Get all user Loans/Applications", response_model=list[LoanDto], responses={
    200: {"description": "Successful operation"},
    400: {"description": "Bad request - malformed request"},
    403: {"description": "Forbidden - insufficient rights to access requested resource"},
    404: {"description": "Resource not found"}
})
def get_loans(natural_person_args: NaturalPersonDependency, search: Optional[str] = None, orderby: Optional[str] = "loan_number", orderdir: Optional[str] = "asc"):
    natural_person_view = natural_person_args.natural_person_view
    db = natural_person_args.db

    if not natural_person_view:
        raise HTTPException(status_code=404, detail="Resource not found")
    
    if orderby not in [column.key for column in LoanView.__table__.columns] or orderdir not in ("asc", "desc"):
        raise HTTPException(status_code=400, detail="Bad request - malformed request")
    
    order_column = LoanView.__table__.columns[orderby]
    if orderdir == "asc":
        order_clause = order_column.asc()
    else:
        order_clause = order_column.desc()

    filters = [LoanView.owner_person_id == natural_person_view.person_id]
    if search:
        filters.append(or_(
            LoanView.loan_title.contains(search),
            LoanView.loan_type_label.contains(search),
            LoanView.loan_status_label.contains(search)
        ))

    stmt = select(LoanView).where(and_(*filters)).order_by(order_clause)
    loan_views = db.execute(stmt).scalars().all()

    results = []
    for loan_view in loan_views:
        results.append(LoanDto.from_view(loan_view))

    return results    

@loan_router.get("/loan", description="Get specific user Loans/Applications", response_model=LoanDto, responses={
    200: {"description": "Successful operation"},
    400: {"description": "Bad request - malformed request"},
    403: {"description": "Forbidden - insufficient rights to access requested resource"},
    404: {"description": "Resource not found"}
})
def get_loan(natural_person_args: NaturalPersonDependency, loan_id: str):
    natural_person_view = natural_person_args.natural_person_view
    db = natural_person_args.db

    if not natural_person_view:
        raise HTTPException(status_code=404, detail="Resource not found")

    stmt = select(LoanView).where(
        LoanView.loan_id == loan_id
    )
    loan_view = db.execute(stmt).scalars().first()

    if not loan_view:
        raise HTTPException(status_code=404, detail="Resource not found")

    if loan_view.owner_person_id != natural_person_view.person_id:
        raise HTTPException(status_code=403, detail="Forbidden - insufficient rights to access requested resource")

    return LoanDto.from_view(loan_view)
