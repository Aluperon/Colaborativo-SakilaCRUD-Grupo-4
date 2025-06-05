from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.schemas.address_schema import AddressCreate, AddressRead, AddressUpdate
from app.controllers import address_controller

router = APIRouter(prefix="/addresses", tags=["Addresses"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[AddressRead])
def list_addresses(db: Session = Depends(get_db)):
    return address_controller.get_all(db)

@router.get("/{address_id}", response_model=AddressRead)
def get_address(address_id: int, db: Session = Depends(get_db)):
    address = address_controller.get_by_id(db, address_id)
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    return address

@router.post("/", response_model=AddressRead)
def create_address(address: AddressCreate, db: Session = Depends(get_db)):
    return address_controller.create(db, address)

@router.delete("/{address_id}")
def delete_address(address_id: int, db: Session = Depends(get_db)):
    address = address_controller.delete(db, address_id)
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    return {"ok": True}

@router.put("/{address_id}", response_model=AddressRead)
def update_address(address_id: int, address: AddressUpdate, db: Session = Depends(get_db)):
    updated = address_controller.update(db, address_id, address)
    if not updated:
        raise HTTPException(status_code=404, detail="Address not found")
    return updated
