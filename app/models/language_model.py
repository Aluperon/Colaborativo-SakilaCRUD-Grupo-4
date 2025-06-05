from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class Language(Base):
    __tablename__ = "language"

    language_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20))
    last_update = Column(DateTime, default=func.now(), onupdate=func.now())
