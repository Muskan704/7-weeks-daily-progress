# List in python 
# Using Square Brackets:
a = [10,20,40,78,-54,45,-55,]
b = ["Apple", "Banana", "Orange", "Strawberry"]
c = [10,"Hello",54,"World"]
print(a)
print(b)
print(c)

# Using list() Constructor
d = list((5,6,"Hello",5.4))
e = list("hello")
print(d)
print(e)

# Creating List with Repeated Elements
f = ["Hiii"] * 5
g = [4] * 4
print(f)
print(g) 

# Internal Representation of Lists
h = [10, "Hello", 40, True]
print(h[0])
print(h[1])
print(h[3])

# Accessing List Elements
i = [10, 20, 30, 40, 50]
print(i[0])
print(i[-1])
print(i[1:4]) # from index 1 to 3

# Adding Elements into List
j = []
j.append(10)
print("After append(10): ", j)

j.insert(0,5)
print("After Insert(0,5)", j)

j.extend([30,40,50])
print("After extend()", j)

j.clear()
print("Deleteing the Entire List", j)

# Updating Elements into List
k = [10, 20, 30]
k[1] = 70
print(k)

# Removing Elements from List
l = [10, 20, 30, 40, 50]
l.remove(30)
print("After Remove(30)", l)

popped_val = l.pop(2)
print("Popped Element", popped_val)
print("After pop(2)", l)

del l[0]
print("After deleting", l)

# Iterating Over Lists
m = ["Mathura", "Aligarh", "Noida"]
for item in m:
    print(item)

# Nested Lists
matrix = [[1,2,3],
          [5,6,7],
          [8,9,10]]
print(matrix[2][2])

# List Comprehension
squares = [x**2 for x in range(1,6)]
print(squares)

'''
def function(a=0,l=[]):
    l.append(a)
    l.append(l)
    return l
fun = function(l=[2,3])
print(fun)

'''