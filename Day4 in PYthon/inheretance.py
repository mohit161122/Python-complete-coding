class Employee:
    start_time = "10am"
    end_time = "6pm"

    def change_time(self, new_end_time):
        self.end_time = new_end_time

class AdminStaff(Employee):
    def __init__(self, role):
        self.role = role

class Accountant(AdminStaff):
    def __init__(self, salery, role):
        super().__init__(role)
        self.salery = salery

        
acc1 = Accountant(25_000 , "CA")

print(acc1.role , acc1.salery , acc1.start_time, acc1.end_time)
       