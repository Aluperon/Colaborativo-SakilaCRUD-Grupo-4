from sqlalchemy import Column, Integer, String, Text
from app.core.database import Base

class FilmText(Base):
    __tablename__ = "film_text"

    film_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    description = Column(Text)
