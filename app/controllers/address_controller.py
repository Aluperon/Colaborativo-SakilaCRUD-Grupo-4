from sqlalchemy.orm import Session
from app.models.address_model import Address
from app.schemas.address_schema import AddressCreate, AddressUpdate

def get_all(db: Session):
    return db.query(Address).all()

def get_by_id(db: Session, address_id: int):
    return db.query(Address).filter(Address.address_id == address_id).first()

def create(db: Session, address_data: AddressCreate):
    address = Address(**address_data.dict())
    db.add(address)
    db.commit()
    db.refresh(address)
    return address

def delete(db: Session, address_id: int):
    address = get_by_id(db, address_id)
    if address:
        db.delete(address)
        db.commit()
    return address

def update(db: Session, address_id: int, address_data: AddressUpdate):
    address = get_by_id(db, address_id)
    if not address:
        return None
    for field, value in address_data.dict(exclude_unset=True).items():
        setattr(address, field, value)
    db.commit()
    db.refresh(address)
    return address
