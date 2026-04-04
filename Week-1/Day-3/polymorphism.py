# Method Overloading

class ShoppingCart:
    def add_item(self, *prices):
        total = 0
        for price in prices:
            total += price
        return total


cart = ShoppingCart()

print(cart.add_item(500))             # one item
print(cart.add_item(500, 1200))        # two items
print(cart.add_item(500, 1200, 300))   # three items

# Method Overriding 

class Vehicle:
    def max_speed(self):
        print("Vehicle speed is 80 km/h")

class Car(Vehicle):
    def max_speed(self):
        print("Car speed is 120 km/h")

class Bike(Vehicle):
    def max_speed(self):
        print("Bike speed is 100 km/h")


v = Vehicle()
c = Car()
b = Bike()

v.max_speed()
c.max_speed()
b.max_speed()

