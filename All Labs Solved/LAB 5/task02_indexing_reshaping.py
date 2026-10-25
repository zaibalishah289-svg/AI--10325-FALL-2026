import numpy as np

# ==========================================
# Task 2 — Indexing, Shapes, and Reshaping
# ==========================================
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("--- Task 2 ---")
print("Element at row 1, col 2:", matrix[1, 2])
print("Second row (slice):", matrix[1, :])
print("Second column (slice):", matrix[:, 1])

reshaped_1_9 = matrix.reshape(1, 9)
reshaped_9_1 = matrix.reshape(9, 1)

print("\nReshaped to (1, 9):\n", reshaped_1_9)
print("Reshaped to (9, 1):\n", reshaped_9_1)