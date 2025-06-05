from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CustomerBase(BaseModel):
    store_id: int
    first_name: str
    last_name: str
    email: Optional[str]
    address_id: int
    active: bool

class CustomerCreate(CustomerBase):
    pass

class CustomerRead(CustomerBase):
    customer_id: int
    create_date: datetime
    last_update: Optional[datetime]

    class Config:
        orm_mode = True

class CustomerUpdate(BaseModel):
    email: Optional[str] = None
    active: Optional[bool] = None

    class Config:
        orm_mode = True
