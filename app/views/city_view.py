from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.schemas.city_schema import CityCreate, CityRead, CityUpdate
from app.controllers import city_controller

router = APIRouter(prefix="/cities", tags=["Cities"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[CityRead])
def list_cities(db: Session = Depends(get_db)):
    return city_controller.get_all(db)

@router.get("/{city_id}", response_model=CityRead)
def get_city(city_id: int, db: Session = Depends(get_db)):
    city = city_controller.get_by_id(db, city_id)
    if not city:
        raise HTTPException(status_code=404, detail="City not found")
    return city
@router.post("/", response_model=CityRead)
def create_city(city: CityCreate, db: Session = Depends(get_db)):
    return city_controller.create(db, city)

@router.delete("/{city_id}")
def delete_city(city_id: int, db: Session = Depends(get_db)):
    city = city_controller.delete(db, city_id)
    if not city:
        raise HTTPException(status_code=404, detail="City not found")
    return {"ok": True}

@router.put("/{city_id}", response_model=CityRead)
def update_city(city_id: int, city: CityUpdate, db: Session = Depends(get_db)):
    updated = city_controller.update(db, city_id, city)
    if not updated:
        raise HTTPException(status_code=404, detail="City not found")
    return updated
