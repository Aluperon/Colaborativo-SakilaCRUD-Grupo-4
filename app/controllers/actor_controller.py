from sqlalchemy.orm import Session
from app.models.actor_model import Actor
from app.schemas.actor_schema import ActorCreate, ActorUpdate

def get_all(db: Session):
    return db.query(Actor).all()

def get_by_id(db: Session, actor_id: int):
    return db.query(Actor).filter(Actor.actor_id == actor_id).first()

def create(db: Session, actor_data: ActorCreate):
    actor = Actor(**actor_data.dict())
    db.add(actor)
    db.commit()
    db.refresh(actor)
    return actor

def delete(db: Session, actor_id: int):
    actor = get_by_id(db, actor_id)
    if actor:
        db.delete(actor)
        db.commit()
    return actor

def update(db: Session, actor_id: int, actor_data: ActorUpdate):
    actor = get_by_id(db, actor_id)
    if not actor:
        return None
    for field, value in actor_data.dict(exclude_unset=True).items():
        setattr(actor, field, value)
    db.commit()
    db.refresh(actor)
    return actor

