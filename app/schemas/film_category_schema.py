from pydantic import BaseModel

class FilmCategoryBase(BaseModel):
    film_id: int
    category_id: int

class FilmCategoryCreate(FilmCategoryBase):
    pass

class FilmCategoryRead(FilmCategoryBase):
    class Config:
        orm_mode = True
