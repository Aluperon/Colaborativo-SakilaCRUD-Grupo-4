from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, LargeBinary
from app.core.database import Base

class Staff(Base):
    __tablename__ = "staff"

    staff_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(45))
    last_name = Column(String(45))
    address_id = Column(Integer, ForeignKey("address.address_id"))
    email = Column(String(50))
    store_id = Column(Integer, ForeignKey("store.store_id"))
    active = Column(Boolean)
    username = Column(String(16))
    password = Column(String(40))
    last_update = Column(DateTime)
    picture = Column(LargeBinary)
