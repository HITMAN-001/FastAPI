from pydantic import BaseModel
from typing import Optional, List, Dict, Any

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

class User(BaseModel):
    username: str
    full_name: Optional[str] = None
    email: str
    location: str = "unknown"