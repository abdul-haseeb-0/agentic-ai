# 📊 NumPy: The Ultimate Numerical Computing Library

![Python](https://img.shields.io/badge/Python-3.x-blue.svg) ![NumPy](https://img.shields.io/badge/NumPy-✔️-green) ![License](https://img.shields.io/badge/License-MIT-brightgreen.svg)

NumPy is a **fundamental** Python library for numerical computations and working with arrays.

## 🔹 Installation
```bash
pip install numpy  # or conda install numpy
```

## 🍁 Core Data Structures
### 🔹 Creating Arrays
```python
import numpy as np

# 1D Array
arr1 = np.array([1, 2, 3])

# 2D Array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

# 3D Array
arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
```

## 📜 Common Operations

### 🔹 Array Attributes
```python
arr.shape   # Dimensions of array
arr.size    # Total number of elements
arr.dtype   # Data type of elements
arr.ndim    # Number of dimensions
```

### 🔹 Creating Special Arrays
```python
np.zeros((3,3))     # 3x3 array of zeros
np.ones((2,2))      # 2x2 array of ones
np.eye(4)           # Identity matrix (4x4)
np.random.rand(3,3) # Random numbers (0-1)
np.arange(0, 10, 2) # Array from 0 to 10 with step 2
np.linspace(0, 1, 5) # 5 equally spaced values between 0 and 1
```

### 🔹 Indexing & Slicing
```python
arr[0]     # First element
arr[-1]    # Last element
arr[1:4]   # Elements from index 1 to 3
arr[:2, 1:] # Slice rows and columns
arr[:, 1]  # Select a single column
```

### 🔹 Mathematical Operations
```python
np.add(arr1, arr2)  # Element-wise addition
np.subtract(arr1, arr2)  # Element-wise subtraction
np.multiply(arr1, arr2)  # Element-wise multiplication
np.dot(arr1, arr2)  # Dot product
np.mean(arr)  # Mean
np.sum(arr)  # Sum
np.min(arr)  # Min value
np.max(arr)  # Max value
np.std(arr)  # Standard deviation
```

### 🔹 Reshaping & Transposing
```python
arr.reshape(2,3)  # Reshape to 2 rows, 3 columns
arr.T  # Transpose array
```

### 🔹 Stacking & Concatenation
```python
np.vstack((arr1, arr2))  # Vertical stacking
np.hstack((arr1, arr2))  # Horizontal stacking
np.concatenate((arr1, arr2), axis=0)  # Concatenation
```

### 🔹 Boolean Masking
```python
arr[arr > 5]  # Get elements greater than 5
arr[(arr > 2) & (arr < 8)]  # Multiple conditions
```

### 🔹 Saving & Loading Data
```python
np.save("array.npy", arr)  # Save array to file
arr_loaded = np.load("array.npy")  # Load array from file
```

### 🔹 Random Sampling
```python
np.random.seed(42)  # Set seed for reproducibility
np.random.randint(0, 100, (3,3))  # Random integers (0-100)
np.random.choice(arr, 5)  # Randomly pick 5 elements
```

---
🌟 **Follow for more Python skills!** 🚀