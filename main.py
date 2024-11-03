from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from crud.crud import get_user_by_id, create_user, get_user_by_email
from db.database import database
from models.models import SessionLocal
from pydantic import BaseModel

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class UserCreate(BaseModel):
    name: str
    email: str

@app.post("/users/")
async def create_user_route(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, name=user.name, email=user.email)

@app.get("/users/{user_id}")
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
