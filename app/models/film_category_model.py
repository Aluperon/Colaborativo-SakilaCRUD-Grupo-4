from sqlalchemy import Column, Integer, ForeignKey, PrimaryKeyConstraint
from app.core.database import Base

class FilmCategory(Base):
    __tablename__ = "film_category"

    film_id = Column(Integer, ForeignKey("film.film_id"), nullable=False)
    category_id = Column(Integer, ForeignKey("category.category_id"), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('film_id', 'category_id'),
    )
