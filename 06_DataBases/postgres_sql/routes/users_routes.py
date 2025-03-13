from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models.models import Users
from validations.validations import UserLogin
from utils.utilities import create_token
from config.database import get_db

users_router = APIRouter()

# user login
@users_router.post("/login")
def user_login(user: UserLogin, db: Session = Depends(get_db)):
    try:
        valid_user = db.query(Users).filter(Users.email == user.email).first()
        if not valid_user:
            raise HTTPException(status_code=404, detail="User not found")
        if valid_user.password != user.password:
            raise HTTPException(status_code=400, detail="Invalid email or password")
        token = create_token(data={
            "email": valid_user.email,
            "name": valid_user.name,
            "id": valid_user.id
        })
        if not token:
            raise HTTPException(status_code=500, detail="Token creation failed")
        user_data = {
            "email": valid_user.email,
            "token": token
        }
        return {
            "data": user_data,
            "status": "success",
            "message": "User logged in"
        }
    except Exception as e:
        return {
            "message": str(e),
            "status": "error",
            "data": None
        }