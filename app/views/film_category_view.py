from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.schemas.film_category_schema import FilmCategoryCreate, FilmCategoryRead, FilmCategoryCreate
from app.controllers import film_category_controller

router = APIRouter(prefix="/film-categories", tags=["FilmCategory"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[FilmCategoryRead])
def list_film_categories(db: Session = Depends(get_db)):
    return film_category_controller.get_all(db)

@router.get("/{film_id}/{category_id}", response_model=FilmCategoryRead)
def get_film_category(film_id: int, category_id: int, db: Session = Depends(get_db)):
    relation = film_category_controller.get_by_ids(db, film_id, category_id)
    if not relation:
        raise HTTPException(status_code=404, detail="Relation not found")
    return relation

@router.post("/", response_model=FilmCategoryRead)
def create_film_category(data: FilmCategoryCreate, db: Session = Depends(get_db)):
    return film_category_controller.create(db, data)

@router.delete("/{film_id}/{category_id}")
def delete_film_category(film_id: int, category_id: int, db: Session = Depends(get_db)):
    relation = film_category_controller.delete(db, film_id, category_id)
    if not relation:
        raise HTTPException(status_code=404, detail="Relation not found")
    return {"ok": True}

@router.put("/{film_id}/{category_id}", response_model=FilmCategoryRead)
def update_film_category(
    film_id: int,
    category_id: int,
    data: FilmCategoryCreate,
    db: Session = Depends(get_db)
):
    updated = film_category_controller.update(db, film_id, category_id, data.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Relation not found")
    return updated
