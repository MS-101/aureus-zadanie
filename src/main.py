
from fastapi import FastAPI

from src.routers import contact_router, loan_router


app = FastAPI(debug=True)

app.include_router(contact_router)
app.include_router(loan_router)
