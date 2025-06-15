from fastapi import FastAPI
from typing import Optional
from models import Item, User

# Create a FastAPI instance
app = FastAPI()

items = []
users = []

# Define a route
@app.get("/")
async def read_root():
    return {"message": "Welcome to FastAPI!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return items[item_id]

@app.post("/items/")
async def create_item(item: Item):
    items.append(item)
    return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    items[item_id] = item
    return {"item_id": item_id, "item": item}

@app.post("/users/")
async def create_user(user: User):
    users.append(user)
    return user

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return users[user_id]

@app.get("/users/")
async def read_all_users():
    return users

# Run with: uvicorn main:app --reload
