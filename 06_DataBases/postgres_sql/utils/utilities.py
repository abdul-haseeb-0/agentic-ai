from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from datetime import datetime, timedelta
from dotenv import load_dotenv
import jwt
import os

load_dotenv()

# OAuth2PasswordBearer instance to handle token extraction from request headers
oauth2scheme = OAuth2PasswordBearer(tokenUrl="token")

# create_token requirements
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

# create encoded token
def create_token(data: dict, expires_delta: Optional[timedelta] = None):
    try:
        to_encode = data.copy()
        expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
        to_encode.update({"exp": expire})
        token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return token
    except Exception as e:
        return None

# decode token
def decode_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except Exception as e:
        print(e)
        return None

# token verification
def verify_token(token: str = Depends(oauth2scheme) ):
    try:
        payload = decode_token(token)
        if payload:
            return {
                "data": payload,
                "message": "token successfully decoded",
                "status": "success"
            }
        if payload is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
    except Exception as e:
        return {
            "message": str(e),
            "status": "error",
            "data": None
        }