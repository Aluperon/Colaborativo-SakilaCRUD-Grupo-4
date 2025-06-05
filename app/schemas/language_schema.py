from pydantic import BaseModel
from datetime import datetime

class LanguageBase(BaseModel):
    name: str

class LanguageCreate(LanguageBase):
    pass

class LanguageRead(LanguageBase):
    language_id: int
    last_update: datetime

    class Config:
        orm_mode = True

class LanguageUpdate(BaseModel):
    name: str | None = None

    class Config:
        orm_mode = True
