from fastapi import FastAPI
from passlib.context import CryptContext
from . import models
from .database import engine
from .routers import user, assettype, asset, auth


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(assettype.router)
app.include_router(asset.router)


@app.get("/")
def root():
    return {"message": "Welcome to my first API built with Python !!!"}
