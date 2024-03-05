# app/crud/crud_concept.py

from sqlalchemy.orm import Session
from app.db.models import Concept

def get_concept(db: Session, concept_id: int):
    return db.query(Concept).filter(Concept.concept_id == concept_id).first()

