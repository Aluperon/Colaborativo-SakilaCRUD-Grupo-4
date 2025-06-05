from sqlalchemy import Column, Integer, String, DateTime
from app.core.database import Base

class Country(Base):
    __tablename__ = "country"

    country_id = Column(Integer, primary_key=True, index=True)
    country = Column(String(50), nullable=False)
    last_update = Column(DateTime, nullable=False)
