
class Teacher:
    total_teacher = 0

    def __init__(self, name):
        self.name = name
        Teacher.total_teacher += 1

    @classmethod
    def get_total(cls):
        return f"Total number of teachers: {cls.total_teacher}"


teacher1 = Teacher("Ram")
teacher2 = Teacher("Sita")
print(Teacher.get_total())
