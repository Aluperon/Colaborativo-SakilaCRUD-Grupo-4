from pydantic import BaseModel
from typing import Optional

class FilmBase(BaseModel):
    title: str
    description: Optional[str] = None
    release_year: Optional[int] = None
    language_id: int
    rental_duration: int
    rental_rate: str
    length: Optional[int] = None
    replacement_cost: str
    rating: Optional[str] = "G"
    special_features: Optional[str] = None

class FilmCreate(FilmBase):
    pass

class FilmRead(FilmBase):
    film_id: int

    class Config:
        orm_mode = True

class FilmUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    release_year: Optional[int] = None
    language_id: Optional[int] = None
    rental_duration: Optional[int] = None
    rental_rate: Optional[str] = None
    length: Optional[int] = None
    replacement_cost: Optional[str] = None
    rating: Optional[str] = None
    special_features: Optional[str] = None

    class Config:
        orm_mode = True
