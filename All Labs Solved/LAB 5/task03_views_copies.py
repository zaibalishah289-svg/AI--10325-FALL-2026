import numpy as np

# ==========================================
# Task 3 — Views and Copies
# ==========================================
a = np.array([1, 2, 3, 4, 5, 6])

# 1. View (Aliasing)
b_view = a[:3]
b_view[0] = 99

print("--- Task 3 ---")
print("Original array 'a' after modifying view:", a)

a[0] = 1  # Resetting

# 2. Independent Copy
b_copy = a[:3].copy()
b_copy[0] = 99

print("Original array 'a' after modifying copy:", a)
print("Independent copy 'b_copy':", b_copy)