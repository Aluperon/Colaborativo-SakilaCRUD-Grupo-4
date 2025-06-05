from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.schemas.actor_schema import ActorCreate, ActorRead, ActorUpdate
from app.controllers import actor_controller

router = APIRouter(prefix="/actors", tags=["Actors"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[ActorRead])
def list_actors(db: Session = Depends(get_db)):
    return actor_controller.get_all(db)

@router.get("/{actor_id}", response_model=ActorRead)
def get_actor(actor_id: int, db: Session = Depends(get_db)):
    actor = actor_controller.get_by_id(db, actor_id)
    if not actor:
        raise HTTPException(status_code=404, detail="Actor not found")
    return actor

@router.post("/", response_model=ActorRead)
def create_actor(actor: ActorCreate, db: Session = Depends(get_db)):
    return actor_controller.create(db, actor)

@router.delete("/{actor_id}")
def delete_actor(actor_id: int, db: Session = Depends(get_db)):
    actor = actor_controller.delete(db, actor_id)
    if not actor:
        raise HTTPException(status_code=404, detail="Actor not found")
    return {"ok": True}

@router.put("/{actor_id}", response_model=ActorRead)
def update_actor(actor_id: int, actor: ActorUpdate, db: Session = Depends(get_db)):
    updated = actor_controller.update(db, actor_id, actor)
    if not updated:
        raise HTTPException(status_code=404, detail="Actor not found")
    return updated
