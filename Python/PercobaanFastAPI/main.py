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