# Register all route here
from View.Animal import AnimalApi
animalRoute = AnimalApi.router


routers = [
    animalRoute
]