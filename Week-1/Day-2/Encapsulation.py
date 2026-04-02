class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance   

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance


acc = BankAccount("Muskan", 1000)

acc.deposit(500)
acc.withdraw(300)

print("Balance:", acc.get_balance())

