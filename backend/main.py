from fastapi import Depends, FastAPI

from .security.auth import get_user

app = FastAPI()


@app.get("/users/me")
def read_user_me(user_token: str = Depends(get_user)):
    return {"token_found": user_token, "message": "welcome"}
