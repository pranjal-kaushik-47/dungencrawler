from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Dummy Server!"}

@app.get("/ping")
def ping():
    return {"response": "pong"}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id, "name": f"Item {item_id}", "description": "This is a dummy item"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "username": f"user{user_id}", "email": f"user{user_id}@example.com"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)