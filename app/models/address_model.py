from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.database import Base

class Address(Base):
    __tablename__ = "address"

    address_id = Column(Integer, primary_key=True, index=True)
    address = Column(String(50), nullable=False)
    address2 = Column(String(50))
    district = Column(String(20), nullable=False)
    city_id = Column(Integer, ForeignKey("city.city_id"), nullable=False)
    postal_code = Column(String(10))
    phone = Column(String(20), nullable=False)
