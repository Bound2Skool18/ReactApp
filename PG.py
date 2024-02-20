import time
class Vehicle:
    def __init__(self,color,brand,model):
        self.color = color
        self.brand = brand
        self.model = model

    def drifting(self):
        time.sleep(2)
        print(f"The all new {self.color} {self.brand} {self.model} is being driving across the highway!")

car = Vehicle("Red","Dodge","Charger")
car.driving()

