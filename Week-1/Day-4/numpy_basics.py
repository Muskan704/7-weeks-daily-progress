#--------------------------------- NUMPY BASICS-----------------------------------------------#
import numpy as np
temperature = np.array([33.2, 31.8, 33.0, 35.2, 36.6])
average = np.mean(temperature)
print(round(average,2))

# creating array from python list
# np.array([ele1, ele2, ele3])
arr_1d = np.array([10,20,30])      # one dimensional array
print(arr_1d)

# two dimensional array or multi-dimensional
arr_2d = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])
print(arr_2d)

# creating array with default values
#np.zeroes(shape) Here, shape is the size for array. ex- (3) for 1D and (3,3)for 2D
zeroes_arr = np.zeros((3,3))
print(zeroes_arr)

# for ones value -> np.ones(shape)
ones_arr = np.ones(3)
print(ones_arr)

# Specific value -> np.full(shape,values)
specific_arr = np.full((2,3),6)
print(specific_arr)

# Create sequences of numbers in numpy
#np.arange(start,stop,step)
arr1 = np.arange(1,20,2)
print(arr1)

# Creating identity matrix
# np.eye(size)
identity_matrix = np.eye(4)
print(identity_matrix)

#---------------------------ARRAY PROPERTIES NAD OPERATIONS-----------------------------------#
# ARRAY PROPERTIES 
#.shape -> shows the size of an array along each dimension.
arr2 = np.array([[1,2,3],
                 [4,5,6]])
print(arr2.shape)
# .size -> Total number of elements in array.
arr3 = np.array([[10,20,30],
                 [40,50,60],
                 [70,80,90]])
print(arr3.size)

# .ndim -> gives the no. of dimensions
a1 = np.array([1,2,3])
a2 = np.array([[10,20,30],[40,50,60]])
a3 = np.array([[[1,2],[3,4],[5,6],[7,8]]])
print(a1.ndim)
print(a2.ndim)
print(a3.ndim)

# .dtype -> It tells the data type of elements.
a4 = np.array([10,20.8,5,3.4])
print(a4.dtype)

#.astype(new.type) -> is a method that helps us to change the data type from one type to another.
a5 = np.array([1.2,2.3,3.4,4.5])
print(a5)
print(a5.dtype)
int_arr = a5.astype(int)
print(int_arr)
print(int_arr.dtype)

# ARRAY OPERATIONS
# Scalar operations
arr = np.array([10,20,30,40,50])
print(arr + 5)   # Adition
print(arr * 2)   # Multiplication
print(arr ** 2)  # power

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
 
print(a + b)    
print(a * b)   
print(a ** 2) 
print(a / b)   

# Aggregation Function
# np.sum(arr) --> add all elem
# np.mean(arr) --> calculate the average
# np.min(arr) --> min value
# np.max(arr) --> max value
# np.std(arr) --> cal standard deviation
# np.var(arr) --> cal variance

c = np.array([10,20,30,40,50,60])
print(np.sum(c))
print(np.mean(c))
print(np.min(c))
print(np.max(c))
print(np.std(c))
print(np.var(c))

# Adding 1D array to each 2D row.
n = np.array([[10,20,30,40,50],
              [60,70,80,90,100]])
l = np.array([1,2,3,4,5])
print("Addition", n+l)

#---------------------------------------------INDEXING AND SLICING ---------------------------------------------------
# Accessing an Element
# array[index] --> 1D and arry[row,col] --> 2D
d = np.array([10,20,30,40,50,60])
print(d[0])
print(d[4])
print(d[-1])
print(d[-3])

# Boolean Indexing
x = np.array([[5, 15, 25, 35, 45]])
print(x[x > 5])
print(x[x % 10 == 5])

# SLICING in Array
# We pass slice instead of index like this: [start:end]. Note: The result includes the start index, but excludes the end index.
# We can also define the step, like this: [start:end:step]
s = np.array([10,20,30,40,50,60])
print(s[1:4])
print(s[2:])
print(s[:4])

# Negative Silicing
print(s[-3:-1])
#Uisng the step value
print(s[1:4:2])
print(s[::2])

# Slicing in 2D array.
t = np.array([[1,2,3,4,5,6],
              [7,8,9,10,11,12]])
print(t[1,1:4])
print(t[0:2,2])
print(t[0:2, 1:4])

# Modifiying elements with the boolean mask
e = np.array([2,-5,-8,6,8,-9,90])
e[e < 0] = 0
print("Changed Value", e)

# np.where — conditional selection
m = np.array([10,54,63,20,90])
result = np.where(m > 25, m, -1)
print(result)

# Universal Function
q = np.array([1,2,3,4,5,6], dtype = float)
print("sqrt",np.sqrt(q))
print("log",np.log(q))
print("exp",np.exp(q))

# Shape manipulation
f = np.arange(6)
print("Original", f)

mat = f.reshape(2,3)
print("Reshaped",mat)

flat = mat.flatten()
print("Flattened",flat)

fi = np.arange(24)
print("Original",fi)
i = fi.reshape(4,-1)
j = fi.reshape(-1,8)
print("Auto reshape", i.shape,j.shape)

# Transpose
matr = np.array([[1,2,3,4,5],
                 [6,7,8,9,10]])
print("Original shape",matr.shape)
print("Transpose Shape",matr.T.shape)

#--------------------------------------------AGGREGATION AND STATISTICS--------------------------------------
matrix = np.array([[10,20,30,40,50],
                   [60,70,80,90,100]])
print("Sum",np.sum(matrix))
print("Col wise sum", np.sum(matrix, axis=0))
print("Row wise Sum",np.sum(matrix, axis=1))
print("cumsum", np.cumsum(m))

# Index of min and max
arry = np.array([10,54,85,36,54,247])
print("argmin:", np.argmin(arry))   # Index of smallest value
print("argmax:", np.argmax(arry))   # Index of largest value

#--------------------Linear Algebra---------------------------
ai = np.array([1, 2, 3])
bi = np.array([4, 5, 6])
print("Dot Product",np.dot(ai,bi))

A = np.array([[1,2],
              [3,4]])
B = np.array([[5,6],
              [7,8]])
print("Matrix multiply", A@B)
print("Determinant",np.linalg.det(A))
print("Inverse",np.linalg.inv(A))