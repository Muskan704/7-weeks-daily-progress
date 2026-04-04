class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def display(self):
        print(self.name,self.salary)

class Manager(Employee):
    def bonus(self):
        print("Bonus",self.salary * 0.2)

m = Manager("Riya",50000)
m.display()
m.bonus()
