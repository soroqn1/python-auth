from database.session import get_db
from database.user import UserCreate
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/register")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    pass


@router.post("/login")
def login_user():
    return {"message": "user logged in"}
