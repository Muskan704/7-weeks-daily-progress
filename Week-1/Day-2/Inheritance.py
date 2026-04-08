class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name:", self.name)


class Student(Person):   
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks

    def display(self):
        self.show()   
        print("Marks:", self.marks)


s = Student("Meghana", 90)
s.display()