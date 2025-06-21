# Basic class definition
class Student:
    def __init__(self, name, college):
        self.name = name
        self.college = college

    def introduce(self):
        return f"My name is {self.name} and I study at {self.college}."


# Creating objects (instances)
student1 = Student("Sita", "Tribhuvan University")
print(student1.introduce())
