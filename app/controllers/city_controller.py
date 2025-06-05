from sqlalchemy.orm import Session
from app.models.city_model import City
from app.schemas.city_schema import CityCreate, CityUpdate

def get_all(db: Session):
    return db.query(City).all()

def get_by_id(db: Session, city_id: int):
    return db.query(City).filter(City.city_id == city_id).first()

def create(db: Session, city_data: CityCreate):
    city = City(**city_data.dict())
    db.add(city)
    db.commit()
    db.refresh(city)
    return city

def delete(db: Session, city_id: int):
    city = get_by_id(db, city_id)
    if city:
        db.delete(city)
        db.commit()
    return city

def update(db: Session, city_id: int, city_data: CityUpdate):
    city = get_by_id(db, city_id)
    if not city:
        return None
    for field, value in city_data.dict(exclude_unset=True).items():
        setattr(city, field, value)
    db.commit()
    db.refresh(city)
    return city
