from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.models import Users
from validations.validations import UserLogin, CreateUser
from utils.utilities import create_token, hash_password, verify_password, verify_api_key
from config.database import get_db

users_router = APIRouter()

# create user
@users_router.post("/create")
def create_user(user: CreateUser, db: Session = Depends(get_db)):
    try:
        new_user = Users(name=user.name, email=user.email, password=hash_password(user.password))
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {
            "data": new_user,
            "status": "success",
            "message": "User created"
        }
    except Exception as e:
        return {
            "message": str(e),
            "status": "error",
            "data": None
        }

# user login
@users_router.post("/login")
def user_login(user: UserLogin, db: Session = Depends(get_db), api_key= Depends(verify_api_key)):
    try:
        valid_user = db.query(Users).filter(Users.email == user.email).first()
        if not valid_user:
            raise HTTPException(status_code=404, detail="User not found")
        if not verify_password(user.password, valid_user.password):
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