from pydantic import BaseModel

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class CategoryRead(CategoryBase):
    category_id: int

class CategoryUpdate(BaseModel):
    name: str | None = None

    class Config:
        orm_mode = True


