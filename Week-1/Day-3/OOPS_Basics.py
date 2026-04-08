# Class example
class student: # Student class
    def greet(self):
        print("Hello Student")

std = student() # std object
std.greet()  # greet method

# Constructor example
class Student:
    def __init__(self,name,age,marks): # __init_ runs automatically
        self.name = name  # self refer to the current object
        self.age = age
        self.marks = marks
    
    def display(self):
        print(self.name,self.age,self.marks)

s = Student("Shreya",21,88)
s.display()

# Instance vs Class Variables
class student: 
    school = "Delhi public school" # class varibale
    def __init__(self,name):
        self.name = name # instance variable
s3 = student("shiv")
s4 = student("Priya")
print(s3.name, s3.school)
print(s4.name,s4.school)

# Types of method
# Instance Method
class Demo:
    school = "DPS School"
    def __init__(self,name):
        self.name = name 
    def instance_method(self):
        print("Instance method",self.name)    
d = Demo("Suhani")
d.instance_method()

# Class Method
class Demo2:
    school = "Bright School"
    def __init__(self,name):
        self.name = name 
    @classmethod # class method decorator
    def class_school(cls):
        cls.school = "ABC school"
Demo2.class_school()
print(Demo2.school)

# Staic Method
class Math:
    @staticmethod
    def add(a,b):
        return a+b
print(Math.add(5,4))





