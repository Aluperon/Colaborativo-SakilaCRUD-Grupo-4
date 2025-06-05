from sqlalchemy.orm import Session
from app.models.category_model import Category
from app.schemas.category_schema import CategoryCreate, CategoryUpdate

def get_all(db: Session):
    return db.query(Category).all()

def get_by_id(db: Session, category_id: int):
    return db.query(Category).filter(Category.category_id == category_id).first()

def create(db: Session, category_data: CategoryCreate):
    category = Category(**category_data.dict())
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

def delete(db: Session, category_id: int):
    category = get_by_id(db, category_id)
    if category:
        db.delete(category)
        db.commit()
    return category

def update(db: Session, category_id: int, category_data: CategoryUpdate):
    category = get_by_id(db, category_id)
    if not category:
        return None
    for field, value in category_data.dict(exclude_unset=True).items():
        setattr(category, field, value)
    db.commit()
    db.refresh(category)
    return category
