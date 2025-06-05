from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class Store(Base):
    __tablename__ = "store"

    store_id = Column(Integer, primary_key=True, index=True)
    manager_staff_id = Column(Integer, ForeignKey("staff.staff_id"))
    address_id = Column(Integer, ForeignKey("address.address_id"))
    last_update = Column(DateTime, default=func.now(), onupdate=func.now())
