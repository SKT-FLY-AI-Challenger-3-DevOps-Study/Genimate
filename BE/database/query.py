from sqlalchemy.orm import Session
from fastapi import HTTPException

from .database import User

def create_email(db: Session, email: str):
    db_email = db.query(User).filter(User.email == email).first()
    if db_email: # db 중복인 경우
        raise HTTPException(status_code=400, detail="User already registered")
    db_email = User(email=email)
    db.add(db_email)
    db.commit()
    db.refresh(db_email)
    return db_email

def read_all_emails(db: Session):
    return db.query(User).all()