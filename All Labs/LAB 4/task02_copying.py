import copy

# Inputs: Raw numerical scores and structured dictionary prediction records
# Processing: Aliasing observation, shallow copying (.copy()), and deep copying (copy.deepcopy())
# Outputs: Comparative console logs demonstrating memory reference behavior and mutability isolation

# --- Part A: Observe the Problem (Aliasing) ---
print("--- Part A: Aliasing Demo ---")
original_scores = [70, 80, 90]
processed_scores = original_scores
processed_scores.append(100)

print("Original:", original_scores)
print("Processed:", processed_scores)


# --- Part B: Fix the Problem (.copy()) ---
print("\n--- Part B: Independent List Copy ---")
original_scores = [70, 80, 90]
processed_scores = original_scores.copy()
processed_scores.append(100)

print("Original:", original_scores)
print("Processed:", processed_scores)


# --- Part C: Shallow Copy vs Deep Copy ---
print("\n--- Part C: Shallow vs Deep Copy ---")
raw_predictions = [
    {"id": 1, "label": "Spam"},
    {"id": 2, "label": "HAM"}
]

# Shallow copy edit
shallow_copy = raw_predictions.copy()
shallow_copy[0]["label"] = "spam"
print("Raw after shallow copy edit:", raw_predictions)

# Recreate raw_predictions for Deep Copy test
raw_predictions = [
    {"id": 1, "label": "Spam"},
    {"id": 2, "label": "HAM"}
]

deep_copied = copy.deepcopy(raw_predictions)
deep_copied[0]["label"] = "spam"

print("Raw after deep copy edit:", raw_predictions)
print("Deep copy:", deep_copied)