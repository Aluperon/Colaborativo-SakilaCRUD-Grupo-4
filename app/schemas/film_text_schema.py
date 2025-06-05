from pydantic import BaseModel

class FilmTextBase(BaseModel):
    title: str
    description: str | None = None

class FilmTextCreate(FilmTextBase):
    pass

class FilmTextRead(FilmTextBase):
    film_id: int

    class Config:
        orm_mode = True

class FilmTextUpdate(BaseModel):
    title: str | None = None
    description: str | None = None

    class Config:
        orm_mode = True
