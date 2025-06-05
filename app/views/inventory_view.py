from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.schemas.inventory_schema import InventoryCreate, InventoryRead, InventoryUpdate
from app.controllers import inventory_controller

router = APIRouter(prefix="/inventory", tags=["Inventory"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[InventoryRead])
def list_inventory(db: Session = Depends(get_db)):
    return inventory_controller.get_all(db)

@router.get("/{inventory_id}", response_model=InventoryRead)
def get_inventory(inventory_id: int, db: Session = Depends(get_db)):
    inventory = inventory_controller.get_by_id(db, inventory_id)
    if not inventory:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return inventory

@router.post("/", response_model=InventoryRead)
def create_inventory(inventory: InventoryCreate, db: Session = Depends(get_db)):
    return inventory_controller.create(db, inventory)

@router.delete("/{inventory_id}")
def delete_inventory(inventory_id: int, db: Session = Depends(get_db)):
    inventory = inventory_controller.delete(db, inventory_id)
    if not inventory:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return {"ok": True}

@router.put("/{inventory_id}", response_model=InventoryRead)
def update_inventory(inventory_id: int, inventory: InventoryUpdate, db: Session = Depends(get_db)):
    updated = inventory_controller.update(db, inventory_id, inventory)
    if not updated:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return updated
