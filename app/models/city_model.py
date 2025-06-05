from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.database import Base

class City(Base):
    __tablename__ = "city"

    city_id = Column(Integer, primary_key=True, index=True)
    city = Column(String(50), nullable=False)
    country_id = Column(Integer, ForeignKey("country.country_id"), nullable=False)
