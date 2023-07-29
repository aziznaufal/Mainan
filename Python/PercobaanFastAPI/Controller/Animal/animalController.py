from Model.Animal import animalModel

class animalController:
    
    def __init__(self) -> None:
        self.animal = animalModel.animal

    def getAllAnimal(self):
        return self.animal.animals

    def getAnimalbyName(self, name):
        the_animal = [animal for animal in self.animal.animals if animal['name'] == name]
        return {'animal' : the_animal[0]}