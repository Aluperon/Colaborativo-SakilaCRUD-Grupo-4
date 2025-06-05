from sqlalchemy.orm import Session
from app.models.staff_model import Staff
from app.schemas.staff_schema import StaffCreate, StaffUpdate
from datetime import datetime

def get_all(db: Session):
    return db.query(Staff).all()

def get_by_id(db: Session, staff_id: int):
    return db.query(Staff).filter(Staff.staff_id == staff_id).first()

def create(db: Session, staff_data: StaffCreate):
    staff = Staff(**staff_data.dict(), last_update=datetime.utcnow())
    db.add(staff)
    db.commit()
    db.refresh(staff)
    return staff

def delete(db: Session, staff_id: int):
    staff = get_by_id(db, staff_id)
    if staff:
        db.delete(staff)
        db.commit()
    return staff

def update(db: Session, staff_id: int, staff_data: StaffUpdate):
    staff = get_by_id(db, staff_id)
    if not staff:
        return None
    for field, value in staff_data.dict(exclude_unset=True).items():
        setattr(staff, field, value)
    staff.last_update = datetime.utcnow()
    db.commit()
    db.refresh(staff)
    return staff
