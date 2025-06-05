from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.schemas.language_schema import LanguageCreate, LanguageRead, LanguageUpdate
from app.controllers import language_controller

router = APIRouter(prefix="/languages", tags=["Languages"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[LanguageRead])
def list_languages(db: Session = Depends(get_db)):
    return language_controller.get_all(db)

@router.get("/{language_id}", response_model=LanguageRead)
def get_language(language_id: int, db: Session = Depends(get_db)):
    language = language_controller.get_by_id(db, language_id)
    if not language:
        raise HTTPException(status_code=404, detail="Language not found")
    return language

@router.post("/", response_model=LanguageRead)
def create_language(language: LanguageCreate, db: Session = Depends(get_db)):
    return language_controller.create(db, language)

@router.delete("/{language_id}")
def delete_language(language_id: int, db: Session = Depends(get_db)):
    language = language_controller.delete(db, language_id)
    if not language:
        raise HTTPException(status_code=404, detail="Language not found")
    return {"ok": True}

@router.put("/{language_id}", response_model=LanguageRead)
def update_language(language_id: int, language: LanguageUpdate, db: Session = Depends(get_db)):
    updated = language_controller.update(db, language_id, language)
    if not updated:
        raise HTTPException(status_code=404, detail="Language not found")
    return updated
