from fastapi import FastAPI, HTTPException
from typing import Optional, List, Dict, Any
from models import Item, User

# In-memory storage
items: List[Item] = []
users: List[User] = []

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
    if item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

@app.post("/items/")
async def create_item(item: Item):
    items.append(item)
    return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    if item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item
    return {"item_id": item_id, "item": item}

@app.post("/users/")
async def create_user(user: User):
    users.append(user)
    return user

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    if user_id >= len(users):
        raise HTTPException(status_code=404, detail="User not found")
    return users[user_id]

@app.get("/users/")
async def read_all_users():
    return users

if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
