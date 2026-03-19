from database.base import Base
from database.session import engine
from fastapi import FastAPI
from routers import user

Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(user.router)
