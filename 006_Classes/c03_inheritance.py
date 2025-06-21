# Parent class
class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return ""


# Child classes
class Dog(Animal):
    def speak(self):
        return f" {self.name} barks !!"


class Cat(Animal):
    def speak(self):
        return f" {self.name} meows !!"


dog = Dog("Tom")
cat = Cat("Jerry")

print(dog.speak())
print(cat.speak())
