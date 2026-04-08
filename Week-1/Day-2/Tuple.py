# Tuple in Python
# Creating a Tuple

t = () 
print(t)

tup = (10, "hello", 20, True)
print(tup)

# Using list
list = [10, 20, "Hello", "Hi"]
print(tuple(list))

tup = tuple("Hello")
print(tup)

# Creating a Tuple with Mixed Datatypes
a = (10, 20, True, "Welcome",[1,2,3,4],{"name:Myra"},4.8)
print(a)

# Tuple Basic Operations
c = tuple("Hello")
print(c[0])
print(c[1:])
print(c[1:3])
print(c[:-1])

#Tuple Unpacking
b = ("Hii","Bihar",True)
x,y,z = b
print(x)
print(y)
print(z)

# Concatenation of Tuples
m = ("Hello","World","Nice")
n = (1,2,3,4)
o = m + n
print(o)

# Slicing of Tuple
z = tuple("HELLOWORLD")
print(z[0])
print(z[::-1])
print(z[1:])
print(z[1:4])

# Deleting a Tuple
u = (1,2,3,4)
del u
#print(u)

t = (1,2,3,4,5,6)
a,*b,c = t
print(a)
print(b)
print(c)