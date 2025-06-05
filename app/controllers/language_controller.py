from sqlalchemy.orm import Session
from app.models.language_model import Language
from app.schemas.language_schema import LanguageCreate, LanguageUpdate

def get_all(db: Session):
    return db.query(Language).all()

def get_by_id(db: Session, language_id: int):
    return db.query(Language).filter(Language.language_id == language_id).first()

def create(db: Session, language_data: LanguageCreate):
    language = Language(**language_data.dict())
    db.add(language)
    db.commit()
    db.refresh(language)
    return language

def delete(db: Session, language_id: int):
    language = get_by_id(db, language_id)
    if language:
        db.delete(language)
        db.commit()
    return language

def update(db: Session, language_id: int, language_data: LanguageUpdate):
    language = get_by_id(db, language_id)
    if not language:
        return None
    for field, value in language_data.dict(exclude_unset=True).items():
        setattr(language, field, value)
    db.commit()
    db.refresh(language)
    return language
