from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PaymentBase(BaseModel):
    customer_id: int
    staff_id: int
    rental_id: int
    amount: float
    payment_date: datetime

class PaymentCreate(PaymentBase):
    pass

class PaymentRead(PaymentBase):
    payment_id: int
    last_update: Optional[datetime]

    class Config:
        orm_mode = True

class PaymentUpdate(BaseModel):
    amount: Optional[float] = None
    payment_date: Optional[datetime] = None

    class Config:
        orm_mode = True
