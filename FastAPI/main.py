from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

items = [{"id": 1, "item": "Computador"}, {"id": 2, "item": "Caderno"}, {"id": 3, "item": "Garrafa"}]

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float

@app.get("/")
async def hello():
    return {"message": "Hello"}

# Query Parameters
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    try:
        response = None
        for item in items:
            if item["id"] == item_id:
                response = item
        if response:
            return response
        else:
            return {"message": "Not Found"}
    except:
        return {'message': "Bad Request"}
    
# Query Parameters
@app.get("/items")
async def read_item(skip: int = 0, limit: int = 10):
    return items[skip : skip + limit]
        
# Request Body
@app.post("/items")
async def create_item(item: Item):
    return {"item_name": item.name, "price": item.price}

@app.put("/itemss/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.model_dump()}

# Query Parameters and String Validations
@app.get("/places")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    # teste: str = Query(default="Teste")
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results