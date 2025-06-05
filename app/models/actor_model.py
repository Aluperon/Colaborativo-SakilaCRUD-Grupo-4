from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Actor(Base):
    __tablename__ = "actor"

    actor_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(45))
    last_name = Column(String(45))
