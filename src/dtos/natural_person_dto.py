from pydantic import BaseModel
from typing import Optional

from .address_dto import AddressDto


class NaturalPersonDto(BaseModel):
    eduid: Optional[int] = None
    title_before: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    title_after: Optional[str] = None
    address: Optional[AddressDto] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None

    model_config = {
        "json_schema_extra": {
            "example": {
                "eduid": "303000001",
                "title_before": "Ing.",
                "first_name": "Meno Klienta",
                "last_name": "Priezvisko Klienta",
                "title_after": "MBA",
                "address": {
                    "country": "Krajina",
                    "city": "Mesto Klienta",
                    "zip_code": "123 45",
                    "street": "Ulica Klienta",
                    "number_s": "1234",
                    "number_o": "2a"
                },
                "email": "email@klienta.sk",
                "phone_number": "421987654321"
            }
        }
    }