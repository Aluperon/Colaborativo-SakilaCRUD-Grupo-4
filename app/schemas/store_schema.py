from pydantic import BaseModel
from datetime import datetime

class StoreBase(BaseModel):
    manager_staff_id: int
    address_id: int

class StoreCreate(StoreBase):
    pass

class StoreRead(StoreBase):
    store_id: int
    last_update: datetime

    class Config:
        orm_mode = True

class StoreUpdate(BaseModel):
    manager_staff_id: int | None = None
    address_id: int | None = None

    class Config:
        orm_mode = True
