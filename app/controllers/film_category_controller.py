from sqlalchemy.orm import Session
from app.models.film_category_model import FilmCategory
from app.schemas.film_category_schema import FilmCategoryCreate

def get_all(db: Session):
    return db.query(FilmCategory).all()

def get_by_ids(db: Session, film_id: int, category_id: int):
    return db.query(FilmCategory).filter(
        FilmCategory.film_id == film_id,
        FilmCategory.category_id == category_id
    ).first()

def create(db: Session, data: FilmCategoryCreate):
    relation = FilmCategory(**data.dict())
    db.add(relation)
    db.commit()
    db.refresh(relation)
    return relation

def delete(db: Session, film_id: int, category_id: int):
    relation = get_by_ids(db, film_id, category_id)
    if relation:
        db.delete(relation)
        db.commit()
    return relation

def update(db: Session, film_id: int, category_id: int, new_data: dict):
    relation = get_by_ids(db, film_id, category_id)
    if not relation:
        return None
    db.delete(relation)
    db.commit()
    updated_relation = FilmCategory(**new_data)
    db.add(updated_relation)
    db.commit()
    db.refresh(updated_relation)
    return updated_relation
