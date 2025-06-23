class Animal:
    def __init__(self, name):
        self.name = name

    def intro(self):
        print(f"The name of animal {self.name}.")
        print("Inside the intro method")
        print(self)


a = Animal("Monkey")
a.intro()
print("Outside Class")
print(a)
