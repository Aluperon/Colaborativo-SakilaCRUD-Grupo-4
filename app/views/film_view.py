from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.schemas.film_schema import FilmCreate, FilmRead, FilmUpdate
from app.controllers import film_controller

router = APIRouter(prefix="/films", tags=["Films"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[FilmRead])
def list_films(db: Session = Depends(get_db)):
    return film_controller.get_all(db)

@router.get("/{film_id}", response_model=FilmRead)
def get_film(film_id: int, db: Session = Depends(get_db)):
    film = film_controller.get_by_id(db, film_id)
    if not film:
        raise HTTPException(status_code=404, detail="Film not found")
    return film

@router.post("/", response_model=FilmRead)
def create_film(film: FilmCreate, db: Session = Depends(get_db)):
    return film_controller.create(db, film)

@router.delete("/{film_id}")
def delete_film(film_id: int, db: Session = Depends(get_db)):
    film = film_controller.delete(db, film_id)
    if not film:
        raise HTTPException(status_code=404, detail="Film not found")
    return {"ok": True}

@router.put("/{film_id}", response_model=FilmRead)
def update_film(film_id: int, film: FilmUpdate, db: Session = Depends(get_db)):
    updated = film_controller.update(db, film_id, film)
    if not updated:
        raise HTTPException(status_code=404, detail="Film not found")
    return updated
