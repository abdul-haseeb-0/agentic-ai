from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, APIKeyHeader
from typing import Optional
from passlib.context import CryptContext
from datetime import datetime, timedelta
from dotenv import load_dotenv
import jwt
import os

load_dotenv()

API_KEY_NAME = "API_KEY_TODOS"
# APIKeyHeader instance to handle token extraction from request headers
apikey_scheme = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

# OAuth2PasswordBearer instance to handle token extraction from request headers
oauth2scheme = OAuth2PasswordBearer(tokenUrl="token")

# create token context
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

# password hashing
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# password hashing
def hash_password(password: str):
    return password_context.hash(password)

# password verification
def verify_password(plain_password: str, hashed_password: str):
    return password_context.verify(plain_password, hashed_password) # returns bool

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
def verify_token(token: str = Depends(oauth2scheme)):
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

# verify api key
def verify_api_key(api_key: str = Depends(apikey_scheme)):
    try:
        valid_api_key = os.getenv("API_KEY")
        if not api_key:
            raise HTTPException(status_code=401, detail="API key missing")
        if api_key == valid_api_key:
            return {
                "message": "API key is valid",
                "status": "success",
                "data": None
            }
        else:
            raise HTTPException(status_code=401, detail="Invalid API key")
    except Exception as e:
        return {
            "message": str(e),
            "status": "error",
            "data": None
        }