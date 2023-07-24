from fastapi import APIRouter, HTTPException, Depends
import re
from sqlalchemy.orm import Session

from database.database import SessionLocal, engine
from database.query import create_email
from database.schemas import User

user_router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@user_router.post("/add", status_code=201)
async def addEmail(user: User, db: Session = Depends(get_db)):
    email = user.model_dump()['email']
    
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"  # 유효성 검사를 위한 정규표현식
    if not re.match(reg, email):
        raise HTTPException(status_code=400, detail="Invalid email")
    
    create_email(db, email)

    return {"detail": "Created"}