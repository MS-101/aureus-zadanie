from datetime import date
from dotenv import load_dotenv
from fastapi import Depends, HTTPException
import os
from sqlalchemy import create_engine, select, URL, and_
from sqlalchemy.orm import sessionmaker, Session
from typing import Annotated, Optional

from src.models import NaturalPersonView


load_dotenv(".env")

db_driver = "postgresql"
db_username = os.environ.get("DB_USERNAME")
db_password = os.environ.get("DB_PASSWORD")
db_host = os.environ.get("DB_HOST")
db_port = os.environ.get("DB_PORT")
db_name = os.environ.get("DB_NAME")

url_object = URL.create(
    db_driver, db_username, db_password, db_host, db_port, db_name
)

engine = create_engine(url_object)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def db_dependency():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class NaturalPersonArgs:
    def __init__(self, natural_person_view: NaturalPersonView, db: Session):
        self.natural_person_view = natural_person_view
        self.db = db

def natural_person_dependency(
    eduid: Optional[int] = None,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
    birth_date: Optional[date] = None,
    person_id: Optional[str] = None,
    db: Session = Depends(db_dependency)
):
    if eduid:
        stmt = select(NaturalPersonView).where(NaturalPersonView.person_id == person_id)
        natural_person_view = db.scalars(stmt).first()
    elif first_name or last_name or birth_date or person_id:
        filters = []

        if first_name:
            filters.append(NaturalPersonView.first_name == first_name)
        if last_name:
            filters.append(NaturalPersonView.last_name == last_name)
        if birth_date:
            filters.append(NaturalPersonView.date_of_birth == birth_date)
        if person_id:
            filters.append(NaturalPersonView.personal_identification_number == person_id)

        stmt = select(NaturalPersonView).where(and_(*filters))
        natural_person_view = db.scalars(stmt).first()
    else:
        raise HTTPException(status_code=403, detail="Bad request - malformed request")

    return NaturalPersonArgs(natural_person_view, db)

NaturalPersonDependency = Annotated[NaturalPersonArgs, Depends(natural_person_dependency)]
