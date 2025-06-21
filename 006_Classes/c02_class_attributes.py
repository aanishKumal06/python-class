class Student:
    # Class attribute (shared by all instances)
    college = "Icp"

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def introduce(self):
        return f"Mero naam {self.name} {self.surname} hoo."


student1 = Student("Raam", "grg")
student2 = Student("Shyam", "Magar")

print(student1.introduce())
print(student1.college)
print(student2.introduce())
