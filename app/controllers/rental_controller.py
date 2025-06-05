from sqlalchemy.orm import Session
from app.models.rental_model import Rental
from app.schemas.rental_schema import RentalCreate, RentalUpdate
from datetime import datetime

def get_all(db: Session):
    return db.query(Rental).all()

def get_by_id(db: Session, rental_id: int):
    return db.query(Rental).filter(Rental.rental_id == rental_id).first()

def create(db: Session, rental_data: RentalCreate):
    rental = Rental(**rental_data.dict(), last_update=datetime.utcnow())
    db.add(rental)
    db.commit()
    db.refresh(rental)
    return rental

def delete(db: Session, rental_id: int):
    rental = get_by_id(db, rental_id)
    if rental:
        db.delete(rental)
        db.commit()
    return rental

def update(db: Session, rental_id: int, rental_data: RentalUpdate):
    rental = get_by_id(db, rental_id)
    if not rental:
        return None
    for field, value in rental_data.dict(exclude_unset=True).items():
        setattr(rental, field, value)
    rental.last_update = datetime.utcnow()
    db.commit()
    db.refresh(rental)
    return rental
