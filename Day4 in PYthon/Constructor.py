class Student:
    def __init__(self,name,cgpa):
        self.name = name
        self.cgpa = cgpa

    def get_cgpa(self):
        return self.cgpa

stu1 = Student("Mohit" , 9.0)
stu2 = Student("Raunk", 8.4)
stu3 = Student("Palak", 9.2)

print(f"{stu1.name} has CGPA = {stu1.get_cgpa()}")
print(f"{stu2.name} has CGPA = {stu2.get_cgpa()}")
print(f"{stu3.name} has CGPA = {stu3.get_cgpa()}")


