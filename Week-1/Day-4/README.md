# NumPy Notes 

> Designed for B.Tech CS/AI students who are practicing hands-on in their own editor.

---

## Table of Contents

1. [Introduction](#-introduction)
2. [Installation & Import](#️-installation--import)
3. [NumPy Arrays](#-numpy-arrays)
4. [Indexing & Slicing](#-indexing--slicing)
5. [Array Operations](#-array-operations)
6. [Shape Manipulation](#-shape-manipulation)
7. [Aggregation & Statistics](#-aggregation--statistics)
8. [Linear Algebra](#-linear-algebra)
9. [Random Module](#-random-module)
10. [Saving & Loading Data](#-saving--loading-data)
11. [NumPy in AI & ML](#-numpy-in-ai--ml)
12. [Common Mistakes & Best Practices](#️-common-mistakes--best-practices)
13. [Quick Cheat Sheet](#-quick-cheat-sheet)
14. [Conclusion](#-conclusion)

---

## 📌 Introduction

### What is NumPy?
NumPy (Numerical Python) is an open-source Python library that provides a powerful N-dimensional array object and tools for fast mathematical operations on data.

### Why NumPy is Important
- **Speed** — Runs on pre-compiled C code; far faster than Python loops.
- **Memory efficiency** — Arrays are stored in contiguous memory blocks.
- **Vectorization** — Operations apply to entire arrays without explicit loops.
- **Foundation** — Pandas, Matplotlib, Scikit-learn, TensorFlow, and PyTorch are all built on top of NumPy.

### Where NumPy is Used

| Domain | Usage |
|---|---|
| Data Science | Data cleaning, transformation, aggregation |
| Machine Learning | Feature matrices, weight initialization, loss computation |
| Deep Learning | Tensor operations before GPU offload |
| Computer Vision | Images represented as pixel arrays |
| Scientific Computing | Simulations and numerical methods |

---

## ⚙️ Installation & Import

- Install using `pip install numpy`
- Always import it with the standard alias: `import numpy as np`
- The alias `np` is a universal convention — every tutorial, team, and library uses it

---

## 🧩 NumPy Arrays

The core object in NumPy is the **ndarray** — an N-dimensional array of homogeneous (same-type) data.

### Creating Arrays

| Function | What it does |
|---|---|
| `np.array()` | Create array from a Python list or tuple |
| `np.arange()` | Range-based array, like Python's `range()` |
| `np.linspace()` | Evenly spaced values between two endpoints |
| `np.zeros()` | Array filled entirely with 0s |
| `np.ones()` | Array filled entirely with 1s |
| `np.eye()` | Identity matrix (1s on diagonal, 0s elsewhere) |
| `np.full()` | Array filled with a specific value |
| `np.empty()` | Uninitialized array — values are arbitrary garbage |

### Key Array Attributes

| Attribute | Meaning |
|---|---|
| `.ndim` | Number of dimensions (1D, 2D, 3D, ...) |
| `.shape` | Tuple showing rows × columns × ... |
| `.size` | Total number of elements |
| `.dtype` | Data type of elements (int64, float32, etc.) |

### Data Types (dtype)
NumPy supports specific types for memory efficiency. Common ones: `int8`, `int32`, `int64`, `float32`, `float64`, `bool_`, `complex64`. You can specify dtype explicitly when creating arrays.

---

## 🔍 Indexing & Slicing

### 1D Arrays
- Indexing works just like Python lists — zero-based, supports negative indices.
- Slicing uses `[start:stop:step]` syntax.

### 2D Arrays
- Elements accessed using `[row, column]` notation.
- A full row is selected with `[i, :]`, a full column with `[:, j]`.
- A submatrix is selected with `[row_start:row_end, col_start:col_end]`.

### Boolean (Conditional) Indexing
- A condition applied to an array returns a boolean array (True/False per element).
- Passing that boolean array back into the original returns only elements where the condition is True.
- Very commonly used for filtering data.

### Fancy Indexing
- You can pass a list of indices to select multiple specific elements at once.
- The result is always a copy, not a view.

---

## ➕ Array Operations

### Element-wise Arithmetic
All standard operators (`+`, `-`, `*`, `/`, `**`, `%`) work element-by-element on arrays of the same shape. No loops needed.

### Broadcasting
Broadcasting allows NumPy to operate on arrays of **different but compatible shapes** by automatically "stretching" the smaller array.

**Rules:**
1. Dimensions are compared from the trailing end.
2. Two dimensions are compatible if they are equal or one of them is 1.
3. The smaller array is virtually repeated to match the larger shape.

Example: Adding a `(1, 3)` array to a `(3, 3)` array applies the row to every row of the matrix.

### Universal Functions (ufuncs)
ufuncs are pre-compiled functions that operate element-wise on arrays. Examples include `np.sqrt`, `np.exp`, `np.log`, `np.sin`, `np.cos`, `np.abs`, `np.round`. They are significantly faster than applying Python math functions in a loop.

---

## 🔄 Shape Manipulation

| Function | What it does |
|---|---|
| `.reshape(m, n)` | Returns a new view with a different shape — no data copied |
| `.ravel()` | Flattens to 1D — returns a **view** (modifying it affects the original) |
| `.flatten()` | Flattens to 1D — returns a **copy** (safe to modify independently) |
| `.T` | Transposes the array — rows become columns and vice versa |
| `np.vstack()` | Stacks arrays vertically (row-wise) |
| `np.hstack()` | Stacks arrays horizontally (column-wise) |
| `np.concatenate()` | Joins arrays along a specified axis |
| `np.split()` | Splits an array into multiple sub-arrays |

> Using `-1` in reshape lets NumPy infer that dimension automatically based on total size.

---

## 📊 Aggregation & Statistics

### Common Functions
`np.sum`, `np.min`, `np.max`, `np.mean`, `np.median`, `np.std`, `np.var`, `np.cumsum`, `np.prod`

All of these work on the full array by default, or along a specific axis.

### The `axis` Parameter — Critical Concept

- `axis=0` → operates **down each column** (collapses rows)
- `axis=1` → operates **across each row** (collapses columns)

Think of it as: "collapse along this axis." If you sum a `(3, 4)` array along `axis=0`, you collapse the rows and get a `(4,)` result.

### Index-based Functions

| Function | What it returns |
|---|---|
| `np.argmin()` | Index of the minimum value |
| `np.argmax()` | Index of the maximum value |
| `np.argsort()` | Indices that would sort the array |
| `np.sort()` | A sorted copy of the array |

---

## 🧮 Linear Algebra

All linear algebra functions live in `np.linalg`.

| Function | What it does |
|---|---|
| `np.dot(a, b)` | Dot product of two arrays |
| `A @ B` | Matrix multiplication (preferred modern syntax) |
| `np.linalg.det(A)` | Determinant of a matrix |
| `np.linalg.inv(A)` | Inverse of a matrix |
| `np.linalg.norm(A)` | Norm (magnitude) of a matrix or vector |
| `np.linalg.eig(A)` | Eigenvalues and eigenvectors |
| `np.linalg.solve(A, b)` | Solve the linear system Ax = b |
| `np.linalg.rank(A)` | Rank of a matrix |

> Use `np.linalg.solve(A, b)` instead of `inv(A) @ b` — it is numerically more stable and faster.

> Use `@` for matrix multiplication and `*` for element-wise multiplication. Confusing the two is a very common bug.

---

## 🎲 Random Module

`np.random` is used for generating random data, simulating distributions, and initializing ML model weights.

| Function | What it generates |
|---|---|
| `np.random.rand()` | Uniform random floats in [0, 1) |
| `np.random.randn()` | Values from standard normal distribution (mean=0, std=1) |
| `np.random.randint()` | Random integers in a given range |
| `np.random.uniform()` | Uniform distribution between custom bounds |
| `np.random.normal()` | Normal distribution with custom mean and std |
| `np.random.choice()` | Random sample from an existing array |
| `np.random.shuffle()` | Shuffles an array in-place |

### Random Seed
Setting a seed with `np.random.seed(n)` makes random output reproducible — essential for debugging and sharing experiments. The modern preferred approach is `np.random.default_rng(seed)`.

---

## 💾 Saving & Loading Data

| Format | Save | Load | Notes |
|---|---|---|---|
| `.npy` | `np.save()` | `np.load()` | Single array, fast, binary |
| `.npz` | `np.savez()` | `np.load()` | Multiple arrays, accessed by key |
| `.txt` / `.csv` | `np.savetxt()` | `np.loadtxt()` | Human-readable, slower |

- Use `.npy` / `.npz` for speed and when sharing between Python scripts.
- Use `.txt` when you need to inspect the data manually or share with non-Python tools.

---

## 🚀 NumPy in AI & ML

NumPy powers almost every stage of a machine learning pipeline — even when higher-level frameworks are used on top.

- **Feature matrices** — Datasets are stored as 2D NumPy arrays of shape `(samples, features)`.
- **Normalization & Standardization** — Scaling input data using min-max or z-score methods, computed via NumPy aggregation functions.
- **One-hot encoding** — Converting categorical labels to binary vectors using `np.eye`.
- **Weight initialization** — Random weights for neural networks are generated using `np.random.randn`.
- **Forward pass** — A single linear layer is just a matrix multiplication `X @ W + b`.
- **Loss computation** — MSE, cross-entropy, and other losses are computed as NumPy expressions.
- **Train/test splitting** — Shuffle indices with `np.random.permutation` and slice arrays.

Even when you use PyTorch or TensorFlow, you often convert to/from NumPy arrays when interfacing with data pipelines and evaluation logic.

---

## ⚠️ Common Mistakes & Best Practices

### View vs. Copy
- Array **slices return views**, not copies. Modifying a slice modifies the original array.
- Use `.copy()` explicitly when you need an independent array.

### Axis Confusion
- `axis=0` collapses rows (works column-wise). `axis=1` collapses columns (works row-wise).
- When in doubt, check `.shape` before and after the operation.

### `*` vs `@`
- `*` is element-wise multiplication. `@` is matrix multiplication.
- Using `*` when you mean matrix multiplication is a silent, hard-to-debug error.

### Integer vs Float Division
- Dividing two integer arrays with `/` gives floats in Python 3 — this is correct behavior.
- Use `//` for floor division if that is your intent.

### Broadcasting Errors
- If shapes are not compatible, NumPy raises a `ValueError`. Always check `.shape` before operating on arrays with different dimensions.

### Best Practices

- Avoid Python loops over array elements — always prefer vectorized operations.
- Specify `dtype` explicitly when memory or precision matters (e.g., `float32` for ML).
- Always use `.copy()` when you need an independent version of a sliced array.
- Use `np.linalg.solve()` instead of computing the inverse manually.
- Use `np.random.default_rng(seed)` instead of `np.random.seed()` in new code.
- Check `.shape` often — shape mismatches are the most common source of bugs.

---

## ✅ Quick Cheat Sheet

### Array Creation

| Function | Description |
|---|---|
| `np.array()` | From list or tuple |
| `np.arange()` | Range-based array |
| `np.linspace()` | n evenly spaced values |
| `np.zeros()` | All zeros |
| `np.ones()` | All ones |
| `np.eye()` | Identity matrix |
| `np.full()` | Filled with a constant |
| `np.empty()` | Uninitialized |

### Array Properties

| Attribute | Meaning |
|---|---|
| `.shape` | Dimensions tuple |
| `.ndim` | Number of dimensions |
| `.size` | Total elements |
| `.dtype` | Element data type |

### Shape Manipulation

| Function | Description |
|---|---|
| `.reshape()` | Change shape (view) |
| `.flatten()` | Collapse to 1D (copy) |
| `.ravel()` | Collapse to 1D (view) |
| `.T` | Transpose |
| `np.vstack()` | Vertical stack |
| `np.hstack()` | Horizontal stack |
| `np.concatenate()` | Join along axis |

### Aggregation

| Function | Description |
|---|---|
| `np.sum()` | Total sum |
| `np.mean()` | Average |
| `np.std()` | Standard deviation |
| `np.var()` | Variance |
| `np.min()` / `np.max()` | Min / Max |
| `np.argmin()` / `np.argmax()` | Index of min / max |
| `np.sort()` | Sorted copy |
| `np.cumsum()` | Cumulative sum |

### Linear Algebra

| Function | Description |
|---|---|
| `np.dot()` | Dot product |
| `A @ B` | Matrix multiplication |
| `np.linalg.det()` | Determinant |
| `np.linalg.inv()` | Inverse |
| `np.linalg.solve()` | Solve Ax = b |
| `np.linalg.eig()` | Eigenvalues & eigenvectors |
| `np.linalg.norm()` | Norm |

### Random

| Function | Description |
|---|---|
| `np.random.rand()` | Uniform [0, 1) |
| `np.random.randn()` | Standard normal |
| `np.random.randint()` | Random integers |
| `np.random.seed()` | Set seed |
| `np.random.choice()` | Sample from array |
| `np.random.shuffle()` | In-place shuffle |

### Save & Load

| Function | Description |
|---|---|
| `np.save()` / `np.load()` | Single array (.npy) |
| `np.savez()` / `np.load()` | Multiple arrays (.npz) |
| `np.savetxt()` / `np.loadtxt()` | Text / CSV format |

---

## Conclusion

NumPy is the foundation of Python's entire data and ML ecosystem. The concepts here — broadcasting, vectorization, shape manipulation, linear algebra — come up constantly in real projects and interviews.

---

