# Set in python
# Creating a Set
s = {1,2,3,4,5}
print(s)

a = set()
print(a)

b = set("Watermelon")
print(b)

# Creating a Set with the use of a List
c = set([10,"hii",20,"Namaste"])
print(c)

# Creating a Set with the use of a Tuple
t = ("HELLO","HII","BYE")
print(set(t))

# Creating a Set with the use of a Dictionary
d = {"hello": 1, "hii":2, "Bye":3}
print(set(d))

f = {1,2.3,4}
print(f)
try:
    print(f[0])
except TypeError as e:
    print(e)

# Adding Elements to a Set
x = {90,80,70,60}
x.add(10)
x.update([20,30])
print(x)

# Accessing a Set
y = {"Hello","Hi","Hyy"}
for i in y:
    print(i, end=" ")
print("\n", "Hello" in y)

# Removing Elements from the Set
# Using th remove and discard.
z = {1,2,3,4,5}
z.remove(2)
print(z)

try:
    z.remove(4)
    print(z)
except TypeError as e:
    print("Error", e)

z.discard(5)
print(z)


