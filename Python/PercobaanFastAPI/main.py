from fastapi import FastAPI
from Config import routerRegistration
import sys


app = FastAPI()
_router = routerRegistration.routers
# _router = RouteApi.router
# app.include_router(RouteApi.animalRoute)

# for route in _router.getAllroute():
#     app.include_router(router=route)

for route in _router:
    app.include_router(router=route)


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/roots")
async def root():
    return {"allRoute": _router}



#under this section is just a tutorial purpose

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

# @app.get("/items/{item_id}")
# async def read_user_item(item_id: str, needy: str):
#     item = {"item_id": item_id, "needy": needy}
#     return item


from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.post("/itemsbody/")
async def create_item(item: Item):
    return item