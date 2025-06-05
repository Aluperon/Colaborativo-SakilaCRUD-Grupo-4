from sqlalchemy.orm import Session
from app.models.country_model import Country
from app.schemas.country_schema import CountryCreate, CountryUpdate
from datetime import datetime

def get_all_countries(db: Session):
    return db.query(Country).all()

def get_country(db: Session, country_id: int):
    return db.query(Country).filter(Country.country_id == country_id).first()

def create_country(db: Session, country: CountryCreate):
    db_country = Country(country=country.country, last_update=datetime.utcnow())
    db.add(db_country)
    db.commit()
    db.refresh(db_country)
    return db_country

def update_country(db: Session, country_id: int, country_data: CountryUpdate):
    db_country = db.query(Country).filter(Country.country_id == country_id).first()
    if db_country:
        db_country.country = country_data.country
        db_country.last_update = datetime.utcnow()
        db.commit()
        db.refresh(db_country)
    return db_country

def delete_country(db: Session, country_id: int):
    db_country = db.query(Country).filter(Country.country_id == country_id).first()
    if db_country:
        db.delete(db_country)
        db.commit()
    return db_country
