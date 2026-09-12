class store:
    count = 0

    def __init__(self,name,price):
        self.name = name
        self.price = price
        store.count += 1

    def get_info(self):
        print(f"price of {self.name} is Rs.{self.price}")

    @classmethod
    def get_count(cls):
        print(f"total products in store = {cls.count}")

stu1 = store("Phone" ," 10K")
stu2 = store("Laptop" ," 40K")
stu3 = store("Pen" ," 10K")


stu1.get_info() 
stu2.get_info() 
stu3.get_info() 

store.get_count()