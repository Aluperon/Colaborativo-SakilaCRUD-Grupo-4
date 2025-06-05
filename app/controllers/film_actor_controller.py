from sqlalchemy.orm import Session
from app.models.film_actor_model import FilmActor
from app.schemas.film_actor_schema import FilmActorCreate

def get_all(db: Session):
    return db.query(FilmActor).all()

def get_by_ids(db: Session, film_id: int, actor_id: int):
    return db.query(FilmActor).filter(
        FilmActor.film_id == film_id,
        FilmActor.actor_id == actor_id
    ).first()

def create(db: Session, data: FilmActorCreate):
    relation = FilmActor(**data.dict())
    db.add(relation)
    db.commit()
    db.refresh(relation)
    return relation

def delete(db: Session, film_id: int, actor_id: int):
    relation = get_by_ids(db, film_id, actor_id)
    if relation:
        db.delete(relation)
        db.commit()
    return relation

def update(db: Session, film_id: int, actor_id: int, new_data: dict):
    relation = get_by_ids(db, film_id, actor_id)
    if not relation:
        return None
    db.delete(relation)
    db.commit()
    updated_relation = FilmActor(**new_data)
    db.add(updated_relation)
    db.commit()
    db.refresh(updated_relation)
    return updated_relation
