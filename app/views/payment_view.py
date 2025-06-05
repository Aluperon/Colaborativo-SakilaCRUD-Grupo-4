from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.schemas.payment_schema import PaymentCreate, PaymentRead, PaymentUpdate
from app.controllers import payment_controller

router = APIRouter(prefix="/payments", tags=["Payments"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[PaymentRead])
def list_payments(db: Session = Depends(get_db)):
    return payment_controller.get_all(db)

@router.get("/{payment_id}", response_model=PaymentRead)
def get_payment(payment_id: int, db: Session = Depends(get_db)):
    payment = payment_controller.get_by_id(db, payment_id)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment

@router.post("/", response_model=PaymentRead)
def create_payment(payment: PaymentCreate, db: Session = Depends(get_db)):
    return payment_controller.create(db, payment)

@router.delete("/{payment_id}")
def delete_payment(payment_id: int, db: Session = Depends(get_db)):
    payment = payment_controller.delete(db, payment_id)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return {"ok": True}

@router.put("/{payment_id}", response_model=PaymentRead)
def update_payment(payment_id: int, payment: PaymentUpdate, db: Session = Depends(get_db)):
    updated = payment_controller.update(db, payment_id, payment)
    if not updated:
        raise HTTPException(status_code=404, detail="Payment not found")
    return updated
