from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.controllers import country_controller 
from app.schemas import country_schema

router = APIRouter(prefix="/countries", tags=["Countries"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[country_schema.CountryRead])
def read_countries(db: Session = Depends(get_db)):
    return country_controller.get_all_countries(db)

@router.get("/{country_id}", response_model=country_schema.CountryRead)
def read_country(country_id: int, db: Session = Depends(get_db)):
    country = country_controller.get_country(db, country_id)
    if not country:
        raise HTTPException(status_code=404, detail="Country not found")
    return country

@router.post("/", response_model=country_schema.CountryRead)
def create_country(country: country_schema.CountryCreate, db: Session = Depends(get_db)):
    return country_controller.create_country(db, country)

@router.put("/{country_id}", response_model=country_schema.CountryRead)
def update_country(country_id: int, country: country_schema.CountryUpdate, db: Session = Depends(get_db)):
    updated = country_controller.update_country(db, country_id, country)
    if not updated:
        raise HTTPException(status_code=404, detail="Country not found")
    return updated

@router.delete("/{country_id}")
def delete_country(country_id: int, db: Session = Depends(get_db)):
    deleted = country_controller.delete_country(db, country_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Country not found")
    return {"message": "Country deleted"}
