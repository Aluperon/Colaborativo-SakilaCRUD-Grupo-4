from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class StaffBase(BaseModel):
    first_name: str
    last_name: str
    address_id: int
    email: Optional[str]
    store_id: int
    active: bool
    username: str
    password: Optional[str]

class StaffCreate(StaffBase):
    picture: Optional[bytes] = None

class StaffRead(StaffBase):
    staff_id: int
    last_update: Optional[datetime]
    picture: Optional[bytes]

    class Config:
        orm_mode = True

class StaffUpdate(BaseModel):
    email: Optional[str] = None
    active: Optional[bool] = None
    password: Optional[str] = None
    picture: Optional[bytes] = None

    class Config:
        orm_mode = True
