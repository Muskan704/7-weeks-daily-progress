#----------------------------------------LINEAR ALGEBRA (VECTORS)-------------------------------------------------

import numpy as np

# Creating the Vectors
# Standard Vector
vec = np.array([1,2,3,4])
print(vec)
print(type(vec))

# --------------------------------------------------------------------------------------------------------------------------
# NOTE: A 1D array shape (3,) is neither a row nor a column vector — it is ambiguous. In ML, always be explicit about shape.
# Row Vector
row = np.array([[1,2,3,4]])
print(row.shape)

# Column Vector
col = np.array([[10],
                [20],
                [30]])
print(col.shape)

# -------------------------------------------------------------------------------------------------------------------------
# Utility Function For Creating the vectors
a = np.zeros(5)   # Create vector with zero element.
print(a)

b = np.ones(4)    # All ones
print(b)

c = np.arange(0,10,2)     # Range of values (start=0, stop=10, step=2)
print(c) 

# Evenly spaced values between two points
d = np.linspace(0,1,5)    # 5 points from 0 to 1.
print(d)   

# --------------------------------------------------------------------------------------------------------------------------
# Vector Properties

e = np.array([10,20,30,40,50,60])
print(e.shape)   # 1D with 6 elem
print(e.size)    # Total ele
print(e.ndim)    # No. of dimension
print(e.dtype)   # Which datatype

# --------------------------------------------------------------------------------------------------------------------------
# Vector Reshaping :- Reshaping changes the shape (structure) without changing the data (values).
f = np.array([1,2,3,4,5,6,7,8])

# Convert 1D to col vector
g = f.reshape(8,1)
print(g.shape)

# Convert 1D to row vector
h = f.reshape(1,8)
print(h.shape)

# Use -1 to let NumPy infer one dimension
col2 = f.reshape(-1,1)
row2 = f.reshape(1,-1)
print(col2.shape)
print(row2.shape)

# NOTE: Use reshape(-1, 1) to convert a 1D feature array into a column vector before feeding into sklearn models — a very common operation.

# --------------------------------------------------------------------------------------------------------------------------
# FLATTENING
matrix = np.array([[10,20,30],[40,50,60],[70,80,90]])
flat = matrix.flatten()     # Always returns a copy
print(flat)
flat2 = matrix.ravel()      # Returns a view when possible (more memory efficient)
print(flat2)

# --------------------------------------------------------------------------------------------------------------------------
# Vector Operations
# Addition and Subtraction
i = np.array([1,2,3])
j = np.array([4,5,6])
print(i+j)
print(i-j)

# Scalar Multiplication
k = np.array([2,34,12,6])
print(2 * k)
print(k / 2)
print(k ** 2)

# Element-wise Operations
l = np.array([1,2,3,4,5])
m = np.array([6,7,8,9,10])
print(l * m)
print(l / m)
print(l % m)
print(np.sqrt(l))
print(np.sqrt(m))

# NOTE: ML Relevance: Element-wise operations are the backbone of loss function computations.errors = predictions - targets → element-wise subtraction on thousands of samples simultaneously.

# --------------------------------------------------------------------------------------------------------------------------
# DOT PRODUCTS
n = np.array([10,20,30,40])
p = np.array([50,60,70,80])

# Using np.dot()
res = np.dot(n,p)
print(res)

# Using @ 
res1 = n @ p
print(res1)

# Manual Way
res2 = np.sum(n * p)
print(res2)
# NOTE: Prefer @ over np.dot() for readability. PEP 465 introduced @ specifically for matrix/vector multiplication.

# USE CASE IN MACHINE LEARNING
# Linear Regression prediction (y = w*x +b )
weights = np.array([0.3,1.2,-0.1])
features = np.array([3.0,1.0,2.0])
bias = 0.8
prediction = np.dot(weights,features) + bias
print(f"Prediction: {prediction:.2f}")

# Similarity check
user_a = np.array([4,5,2,3])
user_b = np.array([1,5,3,4])
sim = np.dot(user_a, user_b)
print("Similarity Check", sim)

# --------------------------------------------------------------------------------------------------------------------------

#  Vector Magnitude & Norms
# L1 Norm --> Manhattam Norm
v1 = np.array([10,20,30,40,54])
l1 = np.linalg.norm(v1, ord=1) # ord=1 tells NumPy to calculate the L1 norm (also called Manhattan norm or Taxicab norm).
print(l1)

# L2 Norm --> Euclidean Norm
l2 = np.linalg.norm(v1)
print(l2)
# Manual verification
manual = np.sqrt(np.sum(v1 ** 2))
print(manual)
# NOTE: ML Use: L2 norm is used in Ridge regularization, computing Euclidean distances, and normalizing vectors.

# L3 Norm --> Max Norm
l3 = np.linalg.norm(v1, ord=np.inf)
print(l3)

v = np.array([1, -2, 3, -4])

print(f"L0 norm (non-zeros): {np.linalg.norm(v, ord=0)}")    
print(f"L1 norm: {np.linalg.norm(v, ord=1)}")    
print(f"L2 norm: {np.linalg.norm(v, ord=2):.4f}")
print(f"L∞ norm: {np.linalg.norm(v, ord=np.inf)}")

# --------------------------------------------------------------------------------------------------------------------------

# Unit Vectors & Normalization
# Normalize to unit vector
x = np.array([3.0,4.0])
unit_v = x / np.linalg.norm(x)
print(unit_v)
print(np.linalg.norm(unit_v))

# General Normalization Function
def normalize(vector):
    norm = np.linalg.norm(vector)
    if norm == 0:
        raise ValueError("Cannot normalize the zero value")
    return vector / norm

y = np.array([2.0,3.0,4.0])
print(normalize(y))

# NOTE: Normalizing a zero vector causes division by zero. Always check norm != 0.
# ML Example: Normalizing a Feature Column
sizes = np.array([500.0,1500.0,3000.0,800.0])
# MIN-MAX Normalization
normalize = (sizes - sizes.min()) / (sizes.min() - sizes.max())
print(normalize)

#L2 Normalization
l2_norm = sizes / np.linalg.norm(sizes)
print(l2_norm)

# ----------------------------------------------------------------------------------------------------------------------
# Angle Between Vectors
# Cosine Similarity
a1 = np.array([1.0,0.0,1.0])
b1 = np.array([1.0,1.0,0.0])
cos_sim = np.dot(a1,b1) / np.linalg.norm(a1) * np.linalg.norm(b1)
print(f"Cosine Similarity: {cos_sim:.4f}")

# Angle in degree
angle_rad = np.arccos(np.clip(cos_sim, -1.0, 1.0))
angle_deg = np.degrees(angle_rad)
print(f"Angle: {angle_deg: 2f}")

# NOTE: Due to floating-point errors, cos_sim might be slightly outside [-1, 1]. Use np.clip(cos_sim, -1.0, 1.0) before np.arccos.

# ----------------------------------------------------------------------------------------------------------------------
# Broadcasting with Vectors
# Scalar Broadcasting to vector
s = np.array([10,20,30])  
print(s + 10)   

A = np.array([[1,2,3],
              [4,5,6]])
B = np.array([10,20,30])
print(A + B)

# Column vs Row Broadcasting
col = np.array([[10],
                [20],
                [30]])
row = np.array([10,20,30])
rel = col + row
print(rel)
# NOTE: Broadcasting is essential for adding biases to layer outputs.output = weights @ inputs + bias — bias is broadcast across all samples in the batch.

