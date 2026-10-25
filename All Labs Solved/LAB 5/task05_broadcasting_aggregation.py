import numpy as np

# ==========================================
# Task 5 — Broadcasting, Aggregations & axis
# ==========================================
features = np.array([
    [10.0, 100.0, 1.0],
    [20.0, 200.0, 2.0],
    [30.0, 300.0, 3.0],
    [40.0, 400.0, 4.0]
])

# Part A — Aggregation
mean_all = np.mean(features)
mean_axis0 = np.mean(features, axis=0)
mean_axis1 = np.mean(features, axis=1)
min_cols = np.min(features, axis=0)
max_cols = np.max(features, axis=0)

print("--- Part A ---")
print("Mean of all values:", mean_all)
print("Mean feature columns (axis=0):", mean_axis0)
print("Mean sample rows (axis=1):", mean_axis1)
print("Min of columns:", min_cols)
print("Max of columns:", max_cols)

# Part B — Broadcasting
centered_features = features - mean_axis0
print("\n--- Part B ---")
print("Centered Features:\n", centered_features)
factors = np.array([1.0, 0.01, 10.0])
scaled_by_factors = centered_features * factors
print("Scaled by factors:\n", scaled_by_factors)

# Part C — Incompatible Shape & Reshaping
row_offsets = np.array([1.0, 2.0, 3.0, 4.0])
row_offsets_reshaped = row_offsets.reshape(4, 1)
result_added = features + row_offsets_reshaped

print("\n--- Part C ---")
print("Resulting shape after adding reshaped offsets:", result_added.shape)
print("Resulting matrix:\n", result_added)