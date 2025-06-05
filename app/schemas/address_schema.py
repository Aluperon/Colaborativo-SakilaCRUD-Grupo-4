from pydantic import BaseModel

class AddressBase(BaseModel):
    address: str
    address2: str | None = None
    district: str
    city_id: int
    postal_code: str | None = None
    phone: str

class AddressCreate(AddressBase):
    pass

class AddressRead(AddressBase):
    address_id: int

    class Config:
        orm_mode = True

class AddressUpdate(BaseModel):
    address: str | None = None
    address2: str | None = None
    district: str | None = None
    city_id: int | None = None
    postal_code: str | None = None
    phone: str | None = None

    class Config:
        orm_mode = True
