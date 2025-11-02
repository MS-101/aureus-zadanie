from fastapi import APIRouter, HTTPException
from sqlalchemy import select, insert, update, func

from src.dependencies import NaturalPersonDependency
from src.dtos import AddressDto, NaturalPersonDto
from src.models import NaturalPerson, NaturalPersonView, NaturalPersonAttribute, NaturalPersonAttributeTypeEnum


contact_router = APIRouter(prefix="/contact", tags=["Contact Info"])

@contact_router.get("/info", response_model=NaturalPersonDto, responses={
    200: {"description": "Successful operation"},
    400: {"description": "Bad request - malformed request"},
    403: {"description": "Forbidden - insufficient rights to access requested resource"},
    404: {"description": "Resource not found"}
})
async def get_contact_info(natural_person_args: NaturalPersonDependency):
    natural_person_view = natural_person_args.natural_person_view

    if not natural_person_view:
        raise HTTPException(status_code=404, detail="Resource not found")

    return NaturalPersonDto(
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


@contact_router.post("/info", status_code=201, response_model=NaturalPersonDto, responses={
    201: {"description": "Successful operation"},
    400: {"description": "Bad request - malformed request"},
    403: {"description": "Forbidden - insufficient rights to access requested resource"}
})
async def post_contact_info(natural_person_dto: NaturalPersonDto, natural_person_args: NaturalPersonDependency):
    db = natural_person_args.db
    natural_person_view = natural_person_args.natural_person_view

    # create or update natural_person

    natural_person_values = {}
    if natural_person_dto.title_before:
        natural_person_values["title_before"] = natural_person_dto.title_before
    if natural_person_dto.first_name:
        natural_person_values["first_name"] = natural_person_dto.first_name
    if natural_person_dto.last_name:
        natural_person_values["last_name"] = natural_person_dto.last_name
    if natural_person_dto.title_after:
        natural_person_values["title_after"] = natural_person_dto.title_after
    if natural_person_dto.email:
        natural_person_values["email"] = natural_person_dto.email
    if natural_person_dto.phone_number:
        natural_person_values["phone_number"] = natural_person_dto.phone_number

    if not natural_person_view:
        stmt = insert(NaturalPerson).values(natural_person_values).returning(NaturalPerson.person_id)

        person_id = db.execute(stmt).scalars().first()
    else:
        person_id = natural_person_view.person_id

        if natural_person_values:
            stmt = update(NaturalPerson).where(
                NaturalPerson.person_id == natural_person_view.person_id
            ).values(natural_person_values)
    
    # update natural_person_attributes

    if natural_person_dto.eduid:
        stmt = update(NaturalPersonAttribute).where(
            NaturalPersonAttribute.person_id == person_id,
            NaturalPersonAttribute.person_attribute_type_id == NaturalPersonAttributeTypeEnum.EDUID.value,
            NaturalPersonAttribute.valid_to == None
        ).values(
            valid_to=func.now()
        )
        db.execute(stmt)

        stmt = insert(NaturalPersonAttribute).values(
            person_id=person_id,
            person_attribute_type_id=NaturalPersonAttributeTypeEnum.EDUID.value,
            created_by=person_id,
            attribute_value={
                "value": natural_person_dto.eduid
            }
        )
        db.execute(stmt)
    
    if natural_person_dto.address:
        

        stmt = select(NaturalPersonAttribute).where(
            NaturalPersonAttribute.person_id == person_id,
            NaturalPersonAttribute.person_attribute_type_id == NaturalPersonAttributeTypeEnum.ADDRESS.value,
            NaturalPersonAttribute.valid_to == None
        )
        natural_person_attribute = db.execute(stmt).scalars().first()
        if natural_person_attribute:
            natural_person_attribute.valid_to = func.now()

            natural_person_attribute_values = {
                "city": natural_person_attribute.attribute_value["value"].get("city"),
                "street": natural_person_attribute.attribute_value["value"].get("street"),
                "country": natural_person_attribute.attribute_value["value"].get("country"),
                "number_o": natural_person_attribute.attribute_value["value"].get("number_o"),
                "number_s": natural_person_attribute.attribute_value["value"].get("number_s"),
                "zip_code": natural_person_attribute.attribute_value["value"].get("zip_code")
            }
        else:
            natural_person_attribute_values = {
                "city": "",
                "street": "",
                "country": "",
                "number_o": "",
                "number_s": "",
                "zip_code": ""
            }

        if natural_person_dto.address.city:
            natural_person_attribute_values["city"] = natural_person_dto.address.city
        if natural_person_dto.address.street:
            natural_person_attribute_values["street"] = natural_person_dto.address.street
        if natural_person_dto.address.country:
            natural_person_attribute_values["country"] = natural_person_dto.address.country
        if natural_person_dto.address.number_o:
            natural_person_attribute_values["number_o"] = natural_person_dto.address.number_o
        if natural_person_dto.address.number_s:
            natural_person_attribute_values["number_s"] = natural_person_dto.address.number_s
        if natural_person_dto.address.zip_code:
            natural_person_attribute_values["zip_code"] = natural_person_dto.address.zip_code

        stmt = insert(NaturalPersonAttribute).values(
            person_id=person_id,
            person_attribute_type_id=NaturalPersonAttributeTypeEnum.ADDRESS.value,
            created_by=person_id,
            attribute_value={
                "value": natural_person_attribute_values
            }
        )
        db.execute(stmt)
    
    db.commit()

    stmt = select(NaturalPersonView).where(NaturalPersonView.person_id == person_id)
    result = db.execute(stmt).scalars().one()

    return NaturalPersonDto(
        eduid=result.eduid,
        title_before=result.title_before,
        first_name=result.first_name,
        last_name=result.last_name,
        title_after=result.title_after,
        address=AddressDto(
            country=result.country,
            city=result.city,
            zip_code=result.zip_code,
            street=result.street,
            number_s=result.number_s,
            number_o=result.number_o
        ),
        email=result.email,
        phone_number=result.phone_number
    )