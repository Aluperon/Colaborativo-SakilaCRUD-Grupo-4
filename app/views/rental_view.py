from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.schemas.rental_schema import RentalCreate, RentalRead, RentalUpdate
from app.controllers import rental_controller

router = APIRouter(prefix="/rentals", tags=["Rentals"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[RentalRead])
def list_rentals(db: Session = Depends(get_db)):
    return rental_controller.get_all(db)

@router.get("/{rental_id}", response_model=RentalRead)
def get_rental(rental_id: int, db: Session = Depends(get_db)):
    rental = rental_controller.get_by_id(db, rental_id)
    if not rental:
        raise HTTPException(status_code=404, detail="Rental not found")
    return rental

@router.post("/", response_model=RentalRead)
def create_rental(rental: RentalCreate, db: Session = Depends(get_db)):
    return rental_controller.create(db, rental)

@router.delete("/{rental_id}")
def delete_rental(rental_id: int, db: Session = Depends(get_db)):
    rental = rental_controller.delete(db, rental_id)
    if not rental:
        raise HTTPException(status_code=404, detail="Rental not found")
    return {"ok": True}

@router.put("/{rental_id}", response_model=RentalRead)
def update_rental(rental_id: int, rental: RentalUpdate, db: Session = Depends(get_db)):
    updated = rental_controller.update(db, rental_id, rental)
    if not updated:
        raise HTTPException(status_code=404, detail="Rental not found")
    return updated
