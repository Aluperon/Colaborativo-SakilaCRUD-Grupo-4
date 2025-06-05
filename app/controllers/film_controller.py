from sqlalchemy.orm import Session
from app.models.film_model import Film
from app.schemas.film_schema import FilmCreate, FilmUpdate

def get_all(db: Session):
    return db.query(Film).all()

def get_by_id(db: Session, film_id: int):
    return db.query(Film).filter(Film.film_id == film_id).first()

def create(db: Session, film_data: FilmCreate):
    film = Film(**film_data.dict())
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

def update(db: Session, film_id: int, film_data: FilmUpdate):
    film = get_by_id(db, film_id)
    if not film:
        return None
    for field, value in film_data.dict(exclude_unset=True).items():
        setattr(film, field, value)
    db.commit()
    db.refresh(film)
    return film
