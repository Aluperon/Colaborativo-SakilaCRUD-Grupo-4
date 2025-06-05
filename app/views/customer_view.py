from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.schemas.customer_schema import CustomerCreate, CustomerRead, CustomerUpdate
from app.controllers import customer_controller

router = APIRouter(prefix="/customers", tags=["Customers"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[CustomerRead])
def list_customers(db: Session = Depends(get_db)):
    return customer_controller.get_all(db)

@router.get("/{customer_id}", response_model=CustomerRead)
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = customer_controller.get_by_id(db, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@router.post("/", response_model=CustomerRead)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    return customer_controller.create(db, customer)

@router.delete("/{customer_id}")
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = customer_controller.delete(db, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return {"ok": True}

@router.put("/{customer_id}", response_model=CustomerRead)
def update_customer(customer_id: int, customer: CustomerUpdate, db: Session = Depends(get_db)):
    updated = customer_controller.update(db, customer_id, customer)
    if not updated:
        raise HTTPException(status_code=404, detail="Customer not found")
    return updated
