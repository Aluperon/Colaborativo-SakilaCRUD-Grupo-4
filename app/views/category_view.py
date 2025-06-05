from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.schemas.category_schema import CategoryCreate, CategoryRead, CategoryUpdate
from app.controllers import category_controller

router = APIRouter(prefix="/categories", tags=["Categories"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[CategoryRead])
def list_categories(db: Session = Depends(get_db)):
    return category_controller.get_all(db)

@router.get("/{category_id}", response_model=CategoryRead)
def get_category(category_id: int, db: Session = Depends(get_db)):
    category = category_controller.get_by_id(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.post("/", response_model=CategoryRead)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return category_controller.create(db, category)

@router.delete("/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    category = category_controller.delete(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"ok": True}

@router.put("/{category_id}", response_model=CategoryRead)
def update_category(category_id: int, category: CategoryUpdate, db: Session = Depends(get_db)):
    updated = category_controller.update(db, category_id, category)
    if not updated:
        raise HTTPException(status_code=404, detail="Category not found")
    return updated
