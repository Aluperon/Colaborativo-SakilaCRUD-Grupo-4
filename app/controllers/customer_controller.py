from sqlalchemy.orm import Session
from app.models.customer_model import Customer
from app.schemas.customer_schema import CustomerCreate, CustomerUpdate
from datetime import datetime

def get_all(db: Session):
    return db.query(Customer).all()

def get_by_id(db: Session, customer_id: int):
    return db.query(Customer).filter(Customer.customer_id == customer_id).first()

def create(db: Session, customer_data: CustomerCreate):
    customer = Customer(**customer_data.dict(), create_date=datetime.utcnow(), last_update=datetime.utcnow())
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer

def delete(db: Session, customer_id: int):
    customer = get_by_id(db, customer_id)
    if customer:
        db.delete(customer)
        db.commit()
    return customer

def update(db: Session, customer_id: int, customer_data: CustomerUpdate):
    customer = get_by_id(db, customer_id)
    if not customer:
        return None
    for field, value in customer_data.dict(exclude_unset=True).items():
        setattr(customer, field, value)
    customer.last_update = datetime.utcnow()
    db.commit()
    db.refresh(customer)
    return customer
