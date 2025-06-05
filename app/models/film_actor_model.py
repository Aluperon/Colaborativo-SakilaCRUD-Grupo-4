from sqlalchemy import Column, Integer, ForeignKey, PrimaryKeyConstraint
from app.core.database import Base

class FilmActor(Base):
    __tablename__ = "film_actor"

    film_id = Column(Integer, ForeignKey("film.film_id"), nullable=False)
    actor_id = Column(Integer, ForeignKey("actor.actor_id"), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('film_id', 'actor_id'),
    )
