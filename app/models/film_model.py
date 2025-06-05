from sqlalchemy import Column, Integer, String, Text, ForeignKey, SmallInteger
from sqlalchemy.types import Enum
from app.core.database import Base

class Film(Base):
    __tablename__ = "film"

    film_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    release_year = Column(Integer)
    language_id = Column(SmallInteger, ForeignKey("language.language_id"), nullable=False)
    rental_duration = Column(SmallInteger, nullable=False)
    rental_rate = Column(String(4), nullable=False)
    length = Column(SmallInteger)
    replacement_cost = Column(String(5), nullable=False)
    rating = Column(Enum("G", "PG", "PG-13", "R", "NC-17"), default="G")
    special_features = Column(String(255))
