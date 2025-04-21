from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/health")
def health_check(db: Session = Depends(get_db)):
    try:
        db.execute(text('SELECT 1'))
        return {"status": "healthy"}
    except Exception as e:
        return {"status": "unhealthy"}