from database.db_control import Base, engine
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordRequestForm
from security.auth import get_user

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/users/me")
def read_user_me(user_token: str = Depends(get_user)):
    return {"token_found": user_token, "message": "welcome"}


@app.post("/login")
def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    # TODO: implement db check
    return {"token": "test-token"}


@app.post("/register")
def register_user(form_data: OAuth2PasswordRequestForm = Depends()):
    # TODO: implement db check
    return {"message": "user registered"}
