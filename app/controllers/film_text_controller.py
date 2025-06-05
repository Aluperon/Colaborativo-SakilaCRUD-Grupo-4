from sqlalchemy.orm import Session
from app.models.film_text_model import FilmText
from app.schemas.film_text_schema import FilmTextCreate, FilmTextUpdate

def get_all(db: Session):
    return db.query(FilmText).all()

def get_by_id(db: Session, film_id: int):
    return db.query(FilmText).filter(FilmText.film_id == film_id).first()

def create(db: Session, data: FilmTextCreate):
    film = FilmText(**data.dict())
    db.add(film)
    db.commit()
    db.refresh(film)
    return film

def delete(db: Session, film_id: int):
    film = get_by_id(db, film_id)
    if film:
        db.delete(film)
        db.commit()
    return film

def update(db: Session, film_id: int, data: FilmTextUpdate):
    film = get_by_id(db, film_id)
    if not film:
        return None
    for field, value in data.dict(exclude_unset=True).items():
        setattr(film, field, value)
    db.commit()
    db.refresh(film)
    return film

