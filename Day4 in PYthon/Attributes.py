class Student:
    college_name = "ABC college"
    PI = 3.1

    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa
        self.PI = 3.145


stu1 = Student("Rahul",9.2)
stu2 = Student("Mohit",8.8)


print(stu1.name)
print(stu1.college_name)
print(Student.college_name)
print(Student.PI)
