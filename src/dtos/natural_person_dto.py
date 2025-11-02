from pydantic import BaseModel
from typing import Optional

from src.models import NaturalPersonView


class AddressDto(BaseModel):
    country: Optional[str] = None
    city: Optional[str] = None
    zip_code: Optional[str] = None
    street: Optional[str] = None
    number_s: Optional[str] = None
    number_o: Optional[str] = None

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

    @classmethod
    def from_view(cls, natural_person_view: NaturalPersonView):
        return cls(
            eduid=natural_person_view.eduid,
            title_before=natural_person_view.title_before,
            first_name=natural_person_view.first_name,
            last_name=natural_person_view.last_name,
            title_after=natural_person_view.title_after,
            address=AddressDto(
                country=natural_person_view.country,
                city=natural_person_view.city,
                zip_code=natural_person_view.zip_code,
                street=natural_person_view.street,
                number_s=natural_person_view.number_s,
                number_o=natural_person_view.number_o
            ),
            email=natural_person_view.email,
            phone_number=natural_person_view.phone_number
        )
