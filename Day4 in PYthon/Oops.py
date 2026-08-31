
# L-2
# class student:
#     subject = "Python"
#     college = "ABC"
#     Year  = "4th Year"


# stu1 = student()
# stu2 = student()
# print(stu1.subject,stu1.college,stu1.Year)
# print(stu2.subject,stu2.college,stu2.Year)

# L-3
# stu1 = student()
# s = set()
# print(type(s))


# class Student:
#     def __init__(self, name, cgpa):
#         self.name = name
#         self.cgpa = cgpa
       

# stu1 = Student("Rahul", 9.0)
# stu2 = Student("Urvashi",8.4)
# stu3 = Student("Shradha",9.2)

# print(stu1.name)
# print(stu1.cgpa)
# print(stu2.name)
# print(stu2.cgpa)
# print(stu3.name)
# print(stu3.cgpa)


## Self constructer

class Student:
    def __init__(self):
        print("Obj is being constructed..")

    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa

    def get_cgpa(self):
        return self.cgpa
       

stu1 = Student("Rahul", 9.0)
stu2 = Student("Urvashi",8.4)
stu3 = Student("Shradha",9.2)

# print(stu1.get_cgpa())
# print(stu2.get_cgpa())


print(f"{stu1.name} has cgpa = {stu1.get_cgpa()}")
print(f"{stu2.name} has cgpa = {stu2.get_cgpa()}")
 


