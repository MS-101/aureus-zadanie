from pydantic import BaseModel
from typing import Optional


class AddressDto(BaseModel):
    country: Optional[str] = None
    city: Optional[str] = None
    zip_code: Optional[str] = None
    street: Optional[str] = None
    number_s: Optional[str] = None
    number_o: Optional[str] = None
