from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class RentalBase(BaseModel):
    rental_date: datetime
    inventory_id: int
    customer_id: int
    return_date: Optional[datetime]
    staff_id: int

class RentalCreate(RentalBase):
    pass

class RentalRead(RentalBase):
    rental_id: int
    last_update: Optional[datetime]

    class Config:
        orm_mode = True

class RentalUpdate(BaseModel):
    return_date: Optional[datetime] = None

    class Config:
        orm_mode = True
