# users.py
from fastapi import APIRouter


loan_router = APIRouter(tags=["Loan"])

@loan_router.get("/loans")
def get_loans():
    return []

@loan_router.get("/loan")
def get_loan():
    return {}

@loan_router.post("/loan")
def post_loan():
    return {}
