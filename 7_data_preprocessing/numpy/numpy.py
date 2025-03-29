import numpy as np



# Create a array
# -------------------------------
arr1 = np.array([1, 2, 3])
# 2D Array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
# 3D Array
arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])


# Properties of the array
# -------------------------------
print(arr2.shape) # (2, 3)
print(arr2.size) # 6
print(arr2.ndim) # 2
print(arr2.dtype) # int32


# Special Arrays
# -------------------------------
np.zeros((2, 3)) # [[0, 0, 0], [0, 0, 0]]
np.ones((2, 3)) # [[1, 1, 1], [1, 1, 1]]
np.full((2, 3), 5) # [[5, 5, 5], [5, 5, 5]]
np.eye(2) # [[1, 0], [0, 1]]
np.random.random((2, 3)) # Random values
np.arange(1, 10, 2)  # Array from 1 to 10 with step 2


# Array Operations
# -------------------------------
arr = np.array([1, 2, 3, 4])

print(arr + 2)  # [3 4 5 6]
print(arr * 3)  # [3 6 9 12]
print(arr / 2)  # [0.5 1.0 1.5 2.0]
print(arr ** 2) # [1 4 9 16]


# Matrix Operations
# -------------------------------
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(A + B)  # Matrix addition
print(A - B)  # Matrix subtraction
print(A @ B)  # Matrix multiplication
print(A.T)    # Transpose of A


# Mathematical Functions
np.mean(arr)  # Mean
np.sum(arr)  # Sum
np.min(arr)  # Min value
np.max(arr)  # Max value
np.std(arr)  # Standard deviation

# slicing and indexing
# -------------------------------
print(arr[0])       # First row
print(arr[-1])      # Last row
print(arr[1:4])     # Rows from index 1 to 3
print(arr[:2, 1:])  # First 2 rows, columns from index 1 onward
print(arr[:, 1])    # Second column (all rows)