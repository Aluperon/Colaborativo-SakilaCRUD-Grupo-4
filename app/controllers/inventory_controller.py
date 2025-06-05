from sqlalchemy.orm import Session
from app.models.inventory_model import Inventory
from app.schemas.inventory_schema import InventoryCreate, InventoryUpdate

def get_all(db: Session):
    return db.query(Inventory).all()

def get_by_id(db: Session, inventory_id: int):
    return db.query(Inventory).filter(Inventory.inventory_id == inventory_id).first()

def create(db: Session, inventory_data: InventoryCreate):
    inventory = Inventory(**inventory_data.dict())
    db.add(inventory)
    db.commit()
    db.refresh(inventory)
    return inventory

def delete(db: Session, inventory_id: int):
    inventory = get_by_id(db, inventory_id)
    if inventory:
        db.delete(inventory)
        db.commit()
    return inventory

def update(db: Session, inventory_id: int, inventory_data: InventoryUpdate):
    inventory = get_by_id(db, inventory_id)
    if not inventory:
        return None
    for field, value in inventory_data.dict(exclude_unset=True).items():
        setattr(inventory, field, value)
    db.commit()
    db.refresh(inventory)
    return inventory
