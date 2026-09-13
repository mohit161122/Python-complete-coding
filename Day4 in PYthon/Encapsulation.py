class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, newBalance):
        self.__balance = newBalance
        


acc1 = BankAccount("Rahul Kumar" , 100_000)
acc1.set_balance(200_000)

print(acc1.name , acc1.get_balance)