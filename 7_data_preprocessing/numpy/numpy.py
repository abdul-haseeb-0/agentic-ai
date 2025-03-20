import numpy as np

# Create a array
# -------------------------------
arr_1d = np.array([1, 2, 3, 4, 5])
print(arr_1d)

# Create a 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d)

# Properties of the array
# -------------------------------
print(arr_2d.shape) # (2, 3)
print(arr_2d.size) # 6
print(arr_2d.ndim) # 2
print(arr_2d.dtype) # int32

