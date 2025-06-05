from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.schemas.film_actor_schema import FilmActorCreate, FilmActorRead,FilmActorCreate
from app.controllers import film_actor_controller

router = APIRouter(prefix="/film-actors", tags=["FilmActor"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[FilmActorRead])
def list_film_actors(db: Session = Depends(get_db)):
    return film_actor_controller.get_all(db)

@router.get("/{film_id}/{actor_id}", response_model=FilmActorRead)
def get_film_actor(film_id: int, actor_id: int, db: Session = Depends(get_db)):
    relation = film_actor_controller.get_by_ids(db, film_id, actor_id)
    if not relation:
        raise HTTPException(status_code=404, detail="Relation not found")
    return relation

@router.post("/", response_model=FilmActorRead)
def create_film_actor(data: FilmActorCreate, db: Session = Depends(get_db)):
    return film_actor_controller.create(db, data)

@router.delete("/{film_id}/{actor_id}")
def delete_film_actor(film_id: int, actor_id: int, db: Session = Depends(get_db)):
    relation = film_actor_controller.delete(db, film_id, actor_id)
    if not relation:
        raise HTTPException(status_code=404, detail="Relation not found")
    return {"ok": True}

@router.put("/{film_id}/{actor_id}", response_model=FilmActorRead)
def update_film_actor(
    film_id: int,
    actor_id: int,
    data: FilmActorCreate,
    db: Session = Depends(get_db)
):
    updated = film_actor_controller.update(db, film_id, actor_id, data.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Relation not found")
    return updated

