from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Database Simulation
db = []

# Data Model
class Item(BaseModel):
    id: int
    name: str
    description: str
    price: float

# Create Item
@app.post("/items/", response_model=Item)
def create_item(item: Item):
    db.append(item)
    return item

# Read All Items
@app.get("/items/", response_model=List[Item])
def get_items():
    return db

# Read Single Item
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

# Update Item
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
    for i, item in enumerate(db):
        if item.id == item_id:
            db[i] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

# Delete Item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for i, item in enumerate(db):
        if item.id == item_id:
            del db[i]
            return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")