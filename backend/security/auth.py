from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_user(token: str = Depends(oauth2_scheme)):
    return token


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return plain_password == hashed_password
