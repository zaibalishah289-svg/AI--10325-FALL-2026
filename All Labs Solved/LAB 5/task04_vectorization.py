import numpy as np

# ==========================================
# Task 4 — Vectorization & Numerical Data Types
# ==========================================
temperatures_c = [0.0, 10.0, 22.5, 30.0, 40.0]

# Python loop implementation
f_list = []
for c in temperatures_c:
    f_list.append((c * 9/5) + 32)

# NumPy vectorized expression
c_array = np.array(temperatures_c)
f_array = (c_array * 9/5) + 32

print("--- Part A ---")
print("Python list loop result:", f_list)
print("NumPy vectorized result:", f_array)
print("Are results equal?", np.allclose(f_list, f_array))

# Part B — Element-Wise Operations
base_scores = np.array([0.70, 0.82, 0.91, 0.77])
score_adjustments = np.array([0.03, -0.02, 0.01, 0.05])
adjusted_scores = base_scores + score_adjustments

print("\n--- Part B ---")
print("Adjusted Scores:", adjusted_scores)
print("Minimum:", np.min(adjusted_scores))
print("Maximum:", np.max(adjusted_scores))
print("Average:", np.mean(adjusted_scores))

# Part C — dtype Matters
pixels = np.array([0, 64, 128, 255], dtype=np.uint8)
print("\n--- Part C ---")
print("Original dtype:", pixels.dtype)
pixels_float = pixels.astype(np.float64)
scaled_pixels = pixels_float / 255.0
print("Scaled pixels:", scaled_pixels)
print("Scaled pixels dtype:", scaled_pixels.dtype)