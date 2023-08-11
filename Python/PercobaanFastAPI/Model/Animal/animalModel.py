from pydantic import BaseModel, Extra



class animal(BaseModel):

    name: str
    type: str


    class Config:
        extra = Extra.forbid
    # def __init__(self, **field):
    #     for key, value in field.items():
    #         if key == "name":
    #             self.name = value
    #         if key == "type":
    #             self.type = value

    # def addAnimals(self, **field):
    #     for key, value in field.items():
    #         if key == "name":
    #             self.name = value
    #         if key == "type":
    #             self.type = value
