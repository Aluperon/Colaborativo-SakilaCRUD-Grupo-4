from sqlalchemy.orm import Session
from app.models.payment_model import Payment
from app.schemas.payment_schema import PaymentCreate, PaymentUpdate
from datetime import datetime

def get_all(db: Session):
    return db.query(Payment).all()

def get_by_id(db: Session, payment_id: int):
    return db.query(Payment).filter(Payment.payment_id == payment_id).first()

def create(db: Session, payment_data: PaymentCreate):
    payment = Payment(**payment_data.dict(), last_update=datetime.utcnow())
    db.add(payment)
    db.commit()
    db.refresh(payment)
    return payment

def delete(db: Session, payment_id: int):
    payment = get_by_id(db, payment_id)
    if payment:
        db.delete(payment)
        db.commit()
    return payment

def update(db: Session, payment_id: int, payment_data: PaymentUpdate):
    payment = get_by_id(db, payment_id)
    if not payment:
        return None
    for field, value in payment_data.dict(exclude_unset=True).items():
        setattr(payment, field, value)
    payment.last_update = datetime.utcnow()
    db.commit()
    db.refresh(payment)
    return payment
