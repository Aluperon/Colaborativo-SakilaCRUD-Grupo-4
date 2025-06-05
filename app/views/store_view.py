from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.schemas.store_schema import StoreCreate, StoreRead, StoreUpdate
from app.controllers import store_controller

router = APIRouter(prefix="/stores", tags=["Stores"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[StoreRead])
def list_stores(db: Session = Depends(get_db)):
    return store_controller.get_all(db)

@router.get("/{store_id}", response_model=StoreRead)
def get_store(store_id: int, db: Session = Depends(get_db)):
    store = store_controller.get_by_id(db, store_id)
    if not store:
        raise HTTPException(status_code=404, detail="Store not found")
    return store

@router.post("/", response_model=StoreRead)
def create_store(store: StoreCreate, db: Session = Depends(get_db)):
    return store_controller.create(db, store)

@router.delete("/{store_id}")
def delete_store(store_id: int, db: Session = Depends(get_db)):
    store = store_controller.delete(db, store_id)
    if not store:
        raise HTTPException(status_code=404, detail="Store not found")
    return {"ok": True}

@router.put("/{store_id}", response_model=StoreRead)
def update_store(store_id: int, store: StoreUpdate, db: Session = Depends(get_db)):
    updated = store_controller.update(db, store_id, store)
    if not updated:
        raise HTTPException(status_code=404, detail="Store not found")
    return updated
