from sqlalchemy.orm import Session
from app.models.store_model import Store
from app.schemas.store_schema import StoreCreate, StoreUpdate

def get_all(db: Session):
    return db.query(Store).all()

def get_by_id(db: Session, store_id: int):
    return db.query(Store).filter(Store.store_id == store_id).first()

def create(db: Session, store_data: StoreCreate):
    store = Store(**store_data.dict())
    db.add(store)
    db.commit()
    db.refresh(store)
    return store

def delete(db: Session, store_id: int):
    store = get_by_id(db, store_id)
    if store:
        db.delete(store)
        db.commit()
    return store

def update(db: Session, store_id: int, store_data: StoreUpdate):
    store = get_by_id(db, store_id)
    if not store:
        return None
    for field, value in store_data.dict(exclude_unset=True).items():
        setattr(store, field, value)
    db.commit()
    db.refresh(store)
    return store
