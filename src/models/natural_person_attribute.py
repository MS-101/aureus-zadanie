from datetime import datetime
from enum import Enum
from sqlalchemy import String, JSON
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional

from . import BaseModel


class NaturalPersonAttributeTypeEnum(Enum):
    ADDRESS = "23a667e2-cd67-424d-be08-35e47c6a405f"
    EDUID = "619da077-4520-4968-8c66-3bc966b26f57"

class NaturalPersonAttribute(BaseModel):
    __tablename__ = "natural_person_attribute"

    person_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    person_attribute_type_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    valid_from: Mapped[datetime] = mapped_column(primary_key=True)
    valid_to: Mapped[Optional[datetime]]
    created_by: Mapped[str]
    deleted_by: Mapped[Optional[str]]
    attribute_value: Mapped[dict] = mapped_column(JSON)
