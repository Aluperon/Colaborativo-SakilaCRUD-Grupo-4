from pydantic import BaseModel

class CityBase(BaseModel):
    city: str
    country_id: int

class CityCreate(CityBase):
    pass

class CityRead(CityBase):
    city_id: int

    class Config:
        orm_mode = True

class CityUpdate(BaseModel):
    city: str | None = None
    country_id: int | None = None

    class Config:
        orm_mode = True
