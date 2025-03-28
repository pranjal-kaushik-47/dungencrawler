from fastapi import FastAPI

from .api import (
    inventory,
    user
)

app = FastAPI()

app.include_router(inventory.router)
app.include_router(user.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Dummy Server!"}
