# app/api/endpoints/endpoint_concept.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import crud_concept
from app.db.session import get_db  # Assuming you have a function to get the DB session

router = APIRouter()

@router.get("/concept/{concept_id}")
def read_concept(concept_id: int, db: Session = Depends(get_db)):
    db_concept = crud_concept.get_concept(db, concept_id=concept_id)
    if db_concept is None:
        raise HTTPException(status_code=404, detail="Concept not found")
    return db_concept
