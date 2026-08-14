import os
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
from typing import Optional
from jose import jwt 

SECRET_KEY = os.getenv("SECRET_KEY", "mi_clave_secreta_super_segura_de_desarrollo_123")

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes= ["bcrypt"],deprecated="auto")

def get_password_hash(password: str) -> str:
    result = pwd_context.hash(password)

    return result

def verify_password (plain_password: str, hashed_password: str) -> bool:
    verification = pwd_context.verify(plain_password, hashed_password)

    return verification



def create_access_token (data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()


    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
   
    to_encode.update({"exp":expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

