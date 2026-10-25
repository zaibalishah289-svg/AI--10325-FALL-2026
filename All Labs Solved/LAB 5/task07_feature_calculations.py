import numpy as np

# ==========================================
# Task 7 — Feature Scaling & Numerical Model Calculations
# ==========================================
feature_matrix = np.array([
    [10.0, 100.0, 5.0],
    [20.0, 150.0, 5.0],
    [30.0, 200.0, 5.0],
    [40.0, 250.0, 5.0]
])

# Part A — Min-Max Scaling
col_min = np.min(feature_matrix, axis=0)
col_max = np.max(feature_matrix, axis=0)
spans = col_max - col_min

safe_spans = np.where(spans == 0, 1.0, spans)
scaled_matrix = (feature_matrix - col_min) / safe_spans
scaled_matrix = np.where(spans == 0, 0.0, scaled_matrix)

print("--- Part A ---")
print("Scaled Feature Matrix:\n", scaled_matrix)
print("All results finite:", np.all(np.isfinite(scaled_matrix)))

# Part B — A Simple Weighted Score
features = np.array([
    [1.0, 2.0],
    [2.0, 3.0],
    [3.0, 4.0]
])
weights = np.array([0.4, 0.6])
bias = 0.5

elementwise_mult = features * weights
weighted_score = features @ weights + bias

print("\n--- Part B ---")
print("Element-wise Multiplication:\n", elementwise_mult)
print("Weighted Score (@ dot product + bias):", weighted_score)