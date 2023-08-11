from Model.Animal import animalModel

animals = [animalModel.animal.parse_obj({'name': 'Ellie', 'type': 'Elephant'}), animalModel.animal.parse_obj(
    {'name': 'Python', 'type': 'Snake'}), animalModel.animal.parse_obj({'name': 'Zed', 'type': 'Zebra'})]


class animalController:

    def __init__(self) -> None:
        self.animal = animalModel.animal

    def getAllAnimal(self):
        return animals

    def getAnimalbyName(self, name : str):
        the_animal = [animal for animal in animals if animal.name == name]
        return the_animal

    def insertAnimal(self, item):
        animals.append(item)
        return animals
