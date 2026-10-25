import numpy as np

# ==========================================
# Task 1 — Array Basics
# ==========================================
arr_1d = np.array([10, 20, 30, 40, 50])
arr_2d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print("--- Task 1: Array Basics ---")
print("1D Array:", arr_1d)
print("1D Shape:", arr_1d.shape, "| Dimensions:", arr_1d.ndim, "| Dtype:", arr_1d.dtype)
print("\n2D Array:\n", arr_2d)
print("2D Shape:", arr_2d.shape, "| Dimensions:", arr_2d.ndim, "| Dtype:", arr_2d.dtype)