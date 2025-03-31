import os

from fastapi import FastAPI

from .api import (
    item,
    user
)

app = FastAPI()

app.include_router(item.router)
app.include_router(user.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Dummy Server!"}

@app.get("/auth/hf")
def get_token():
    return os.environ.get("HF_TOKEN")
