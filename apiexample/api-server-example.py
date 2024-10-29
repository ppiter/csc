from fastapi import FastAPI

from pydantic import BaseModel

from typing import Optional

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/request/{symbol}")
async def root(symbol: str):
    return {"message": "Here is the symbol",
            "symbol": symbol}

@app.post("/items/")
async def create_item(item: Item):
    item.name = 'NMAE'
    item.description = "desc"
    item.price = 11
    return item