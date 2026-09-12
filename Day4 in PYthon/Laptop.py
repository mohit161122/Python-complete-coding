class Laptop:
    storage_type = "ssd"

    def __init__(self, Ram, Storage):
        self.Ram = Ram
        self.Storage = Storage

    @classmethod
    def get_storage_type(cls):
        print(f"Storage Type = {cls.storage_type}")

    def get_info(self):
        print(f"Laptop has {self.Ram} Ram & {self.Storage} Stoage and {self.storage_type}")

    @staticmethod
    def cal_dicount(price , dicount):
        final_price = price - (dicount * price /100)
        print(f"Discount price = {final_price}")
        
        

L1 = Laptop("16GB" , "512GB")

L1.cal_dicount(40000,10)




