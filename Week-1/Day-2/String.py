# Strings in python

str1 = "Hello"
print(str1)

#Accessing specific character
str2= "UttarPradesh"
print(str2[0])
print(str2[4])
print(str2[-4])
print(str2[-2])

#Silicing in Strings
str3 = "Rajasthan"
print(str3[0:2])
print(str3[1:4])
print(str3[:3])
print(str3[4:])
print(str3[::-1])
print(str3[0::])

#String Iteration
s = "MadhyaPradesh"
for char in s:
    print(char)

#Replacing First Character
str4 = "Gujarat"
s1 = "g" + str4[1:]
print(s1)

#Delete a String
s2 = "Hello"
del s2

#Update String
a = "happy Birthday"
b = "H" + a[1:]
c = a.replace("Birthday", "Aniversary")
print(b)
print(c)

#String Methods
#len()
print(len(a))

#upper and lower case
print(a.upper())
print(b.lower())

#Strip and replace
x = "    hello   "
y = "My name is Shreya"
print(x.strip())
print(y.replace("Shreya", "Mahi"))

#Concatenating and Repeating Strings
y = "Hello"
z = "World"
print(y+" "+z)

g = "Hello "
print(g * 3)

#Formatting Strings
# f-string
name = "Myra"
age = 21
print(f"Name: {name}, Age: {age}")

#format()
f = "My name is {} and I'm {} year old".format("Meghana",21)
print(f)

#String Membership Testing
d = "Hello World"
print("Hello" in d)
print("Bye" in d)