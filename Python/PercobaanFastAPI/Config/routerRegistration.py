# Register all route here
from Route.Animal import AnimalApi
animalRoute = AnimalApi.router


routers = [
    animalRoute
]