from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from app.core.database import Base

class Customer(Base):
    __tablename__ = "customer"

    customer_id = Column(Integer, primary_key=True, index=True)
    store_id = Column(Integer, ForeignKey("store.store_id"))
    first_name = Column(String(45))
    last_name = Column(String(45))
    email = Column(String(50))
    address_id = Column(Integer, ForeignKey("address.address_id"))
    active = Column(Boolean)
    create_date = Column(DateTime)
    last_update = Column(DateTime)
