from pydantic import BaseModel

class CountryBase(BaseModel):
    country: str

class CountryCreate(CountryBase):
    pass

class CountryRead(CountryBase):
    country_id: int

class CountryUpdate(BaseModel):
    country: str | None = None

    class Config:
        orm_mode = True
