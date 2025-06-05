from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class Inventory(Base):
    __tablename__ = "inventory"

    inventory_id = Column(Integer, primary_key=True, index=True)
    film_id = Column(Integer, ForeignKey("film.film_id"))
    store_id = Column(Integer, ForeignKey("store.store_id"))
    last_update = Column(DateTime, default=func.now(), onupdate=func.now())
