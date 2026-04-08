# MATRICES IN LINEAR 

import numpy as np
# Creating Matrix
# Using python list
A = np.array([[10,20,30],
              [40,50,60],
              [70,80,90]])
print(A)
print(A.shape)

# Utility Function
B = np.zeros((4,3))   # Zeroes
print(B)

C = np.ones((5,2))   # Ones
print(C)

I = np.eye(4)    # Identity
print(I)

D = np.diag([1,2,3,4])   # Diagonal Matrix with diff ele.
print(D)

# -------------------------------------------------------------------------------------------------------------------------
# Random Matrices
# Uniform Distribution [0,1)
R1 = np.random.rand(3,3)
print(R1)

# Standard normal distribution (mean=0, std=1)
R2 = np.random.randn(3,3)
print(R2)

# Random Integer
R3 = np.random.randint(0,10,size=(3,3))   # Values included from 0 - 10
print(R3)

# For reproducibility — always set seed in ML experiments
np.random.seed(42)
W = np.random.randn(3,4) # Weight matrix for a layer
print(W)
# NOTE:Always use np.random.seed(42) at the start of ML experiments for reproducibility.

# -------------------------------------------------------------------------------------------------------------------------
#  Matrix Properties
a = np.array([[1,2,3,4],
              [5,6,7,8]])
print(a.shape)   # (2,3) --> 2 row and 4 col
print(a.size)    
print(a.ndim)
print(a.dtype)

# Accessing Row and column
print(a[0])
print(a[:,1])
print(a[1,3])

# Transpose of a Matrix
b = np.array([[1,2],
              [3,4],
              [5,6]])
print(b.shape)
print(b.T.shape)
print(b.T)
print(np.transpose(b))  # Equivalent

# NOTE: ML Relevance: Transpose is critical in the backpropagation algorithm.Forward: Y = W @ X → Gradient: dW = dY @ Xᵀ

# -------------------------------------------------------------------------------------------------------------------------
# Matrix Operation
# Addition and Subtraction
E = np.array([[1,2],[3,4],[5,6]])
F = np.array([[7,8],[9,10],[11,12]])
print(E + F)
print(E - F)

# Scalar Multiplication
print(3 * E)
print(E / 2)

# Element-wise Multiplication (Hadamard Product)
G = np.array([[1,2],[3,4]])
H = np.array([[5,6],[7,8]])
GH = G * H
print(GH)

# Matrix Multiplication
X = np.array([[1,2],
              [3,4],
              [5,6]])   # (3,2)
Y =np.array([[1,2,3],
             [4,5,6]])
Z = np.dot(X,Y)
print(Z)
print(Z.shape)

z = X @ Y
print(z)
print(np.array_equal(Z, z))

# Element-wise vs Matrix Multiplication
M = np.array([[1, 2], [3, 4]])
N = np.array([[2, 0], [1, 3]])
print("Element wise(M*N):\n",M * N)
print("Matrix Multipliaction (M @ N):\n",M @ N)

# ------------------------------------------------------------------------------------------------------------------------
# Special Matrix Operations
print(M.T)

#Identity matrix
i = np.eye(4)
print(i)

print(M @ np.eye(2))

# Diagonal Matrices
Q = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
dia = np.diag(Q)
print(dia)

# Diagonal Matrix with won ele.
diagonal = np.diag([1,2,3,4])
print(diagonal)

# Symmetric Matrix
Ti = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
sym = np.array_equal(Ti,Ti.T)
print(sym)

# NOTE: ML Relevance: Covariance matrices are always symmetric — crucial for PCA and Gaussian distributions.

# --------------------------------------------------------------------------------------------------------------------------
# Determinant, Inverse & Rank
O = np.array([[3,1],
              [2,4]])
det = np.linalg.det(O)
print(f"Determinant det(O): {det:.2f}")

P = np.array([[1, 2, 3],
              [0, 1, 4],
              [5, 6, 0]])
print(f"Determinant of det(p) = {np.linalg.det(P):.2f}")

# Matrix Inverse
P_inv = np.linalg.inv(P)
print(f"Inverse:",P_inv)

pro = P * P_inv
print("P * P_inv",np.round(pro,10))

# NOTE Important: Never compute A_inv @ b to solve Ax = b in production — it's numerically unstable and slow. Use np.linalg.solve(A, b) instead.

# Matrix Rank
w = np.array([[3,1],
              [2,4]])
print(np.linalg.matrix_rank(w))

x = np.array([[1, 2, 3],
              [0, 1, 4],
              [5, 6, 0]])
print(np.linalg.matrix_rank(x))

# NOTE ML Relevance: Low-rank matrices appear in recommender systems (matrix factorization). A rank-deficient feature matrix indicates multicollinearity — some features are redundant.

# ---------------------------------------------------------------------------------------------------------------------------
#  Linear Systems of Equations
AI = np.array([[3.0, 1.0],
              [2.0, 4.0]])
BI = np.array([9.0, 22.0])
xi = np.linalg.solve(AI,BI)
print(xi)

print(np.allclose(AI @ xi, BI)) # Verify: Ax should equal b

# When the System Has No Unique Solution
# Singular matrix (det = 0) → no unique solution
A_singular = np.array([[1.0, 2.0],
                        [2.0, 4.0]])   
bi = np.array([3.0, 6.0])

try:
    x = np.linalg.solve(A_singular, bi)
except np.linalg.LinAlgError as e:
    print(f"Error: {e}")   # Singular matrix

# Least Squares Solution (Overdetermined Systems)
u = np.array([[1, 1],
              [1, 2],
              [1, 3],
              [1, 4]])  
v = np.array([2.1, 3.9, 6.1, 7.9])

# Least squares solution (minimizes ||Ax - b||²)
x, residuals, rank, sv = np.linalg.lstsq(u, v, rcond=None)
print(x)   # approximately [0.2, 1.94]  (intercept ≈ 0.2, slope ≈ 2)

# --------------------------------------------------------------------------------------------------------------------
# Eigenvalues & Eigenvectors
J = np.array([[4.0, 1.0],
              [2.0, 3.0]])

eigenvalues, eigenvectors = np.linalg.eig(J)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors (columns):\n", eigenvectors)

# Verify: A @ v = λ × v
v1 = eigenvectors[:, 0]   # first eigenvector
lambda1 = eigenvalues[0]  # first eigenvalue
print(np.allclose(A @ v1, lambda1 * v1))   

# Why Eigenvalues Matter in ML
# Covariance matrix — symmetric, so eigenvalues are real
data = np.array([[2.0, 0.0],
                 [0.0, 0.5],
                 [2.2, 0.1],
                 [1.9, 0.0]])

cov = np.cov(data.T)   # Covariance matrix
eigenvalues, eigenvectors = np.linalg.eig(cov)

print("Variance explained by each component:")
total = np.sum(eigenvalues)
for i, ev in enumerate(eigenvalues):
    print(f"  PC{i+1}: {ev/total*100:.1f}%")

## ML Appli.:- PCA (Principal Component Analysis) ,Graph Neural Networks, Stability Analysis.