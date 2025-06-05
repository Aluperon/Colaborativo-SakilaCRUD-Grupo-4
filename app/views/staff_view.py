from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.schemas.staff_schema import StaffCreate, StaffRead, StaffUpdate
from app.controllers import staff_controller

router = APIRouter(prefix="/staff", tags=["Staff"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[StaffRead])
def list_staff(db: Session = Depends(get_db)):
    return staff_controller.get_all(db)

@router.get("/{staff_id}", response_model=StaffRead)
def get_staff(staff_id: int, db: Session = Depends(get_db)):
    staff = staff_controller.get_by_id(db, staff_id)
    if not staff:
        raise HTTPException(status_code=404, detail="Staff not found")
    return staff

@router.post("/", response_model=StaffRead)
def create_staff(staff: StaffCreate, db: Session = Depends(get_db)):
    return staff_controller.create(db, staff)

@router.delete("/{staff_id}")
def delete_staff(staff_id: int, db: Session = Depends(get_db)):
    staff = staff_controller.delete(db, staff_id)
    if not staff:
        raise HTTPException(status_code=404, detail="Staff not found")
    return {"ok": True}

@router.put("/{staff_id}", response_model=StaffRead)
def update_staff(staff_id: int, staff: StaffUpdate, db: Session = Depends(get_db)):
    updated = staff_controller.update(db, staff_id, staff)
    if not updated:
        raise HTTPException(status_code=404, detail="Staff not found")
    return updated
