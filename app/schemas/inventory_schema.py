from pydantic import BaseModel
from datetime import datetime

class InventoryBase(BaseModel):
    film_id: int
    store_id: int

class InventoryCreate(InventoryBase):
    pass

class InventoryRead(InventoryBase):
    inventory_id: int
    last_update: datetime

    class Config:
        orm_mode = True

class InventoryUpdate(BaseModel):
    film_id: int | None = None
    store_id: int | None = None

    class Config:
        orm_mode = True
