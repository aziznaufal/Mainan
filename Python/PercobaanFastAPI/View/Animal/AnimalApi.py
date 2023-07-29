from Model.Animal import animalModel
from Controller.Animal import animalController
from fastapi import APIRouter, Depends, HTTPException


router = APIRouter(
    prefix="/animals",
    tags=["animals"],
    responses={404: {"description": "Not found"}},
)

_animalCon = animalController.animalController()

@router.get("/")
async def root():
    return _animalCon.getAllAnimal()

@router.get("/{animalname}")
async def root(animalname):
    return _animalCon.getAnimalbyName(animalname)