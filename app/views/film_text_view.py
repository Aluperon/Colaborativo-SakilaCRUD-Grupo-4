from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.schemas.film_text_schema import FilmTextCreate, FilmTextRead, FilmTextUpdate
from app.controllers import film_text_controller

router = APIRouter(prefix="/film-texts", tags=["FilmText"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[FilmTextRead])
def list_film_texts(db: Session = Depends(get_db)):
    return film_text_controller.get_all(db)

@router.get("/{film_id}", response_model=FilmTextRead)
def get_film_text(film_id: int, db: Session = Depends(get_db)):
    film = film_text_controller.get_by_id(db, film_id)
    if not film:
        raise HTTPException(status_code=404, detail="Film text not found")
    return film

@router.post("/", response_model=FilmTextRead)
def create_film_text(data: FilmTextCreate, db: Session = Depends(get_db)):
    return film_text_controller.create(db, data)

@router.put("/{film_id}", response_model=FilmTextRead)
def update_film_text(film_id: int, data: FilmTextUpdate, db: Session = Depends(get_db)):
    updated = film_text_controller.update(db, film_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Film text not found")
    return updated

@router.delete("/{film_id}")
def delete_film_text(film_id: int, db: Session = Depends(get_db)):
    film = film_text_controller.delete(db, film_id)
    if not film:
        raise HTTPException(status_code=404, detail="Film text not found")
    return {"ok": True}
