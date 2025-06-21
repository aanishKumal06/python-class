class Vehicle:
    def __init__(self, name):
        self.name = name

    def start(self):
        return f"{self.name} start bhayoo!"


class Car(Vehicle):

    def __init__(self, name, doors):
        super().__init__(name)  # Call parent constructor
        self.doors = doors

    def honk(self):
        return "Poopp Pooop !"


my_car = Car("Toyota", 4)
print(my_car.start())
print(my_car.honk())
