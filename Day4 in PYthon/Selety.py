class Teacher:
    def __init__(self, salary):
        self.salary = salary

class Student:
    def __init__(self, gpa):
        self.gpa = gpa

class TA(Teacher , Student):
    def __init__(self, salary, gpa , name):
        super().__init__(salary)
        Student.__init__(self , gpa)
        self.name = name

Ta1 - TA(15000, 9.3,"mohit")

print(Ta)
