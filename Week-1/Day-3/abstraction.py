from abc import ABC , abstractmethod
class Payment(ABC):
    def pay(self,amount):
        pass
class UPI(Payment):
    def pay(self,amount):
        print(f"Amount {amount} is paid using the UPI.")
class CreditCard(Payment):
    def pay(self,amount):
        print(f"Amount {amount} is paid by using the Credit Card.")

p1 = UPI()
p2 = CreditCard()
p1.pay(4200)
p2.pay(1200)