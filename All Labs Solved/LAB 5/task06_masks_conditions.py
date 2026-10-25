import numpy as np

# ==========================================
# Task 6 — Boolean Masks, Validation & np.where()
# ==========================================
confidence_scores = np.array([0.94, 0.79, -0.10, 0.88, 1.20, 0.63, 0.81])

# Part A — Validate
validity_mask = (confidence_scores >= 0.0) & (confidence_scores <= 1.0)
valid_scores = confidence_scores[validity_mask]
invalid_count = np.sum(~validity_mask)
valid_count = np.sum(validity_mask)

print("--- Part A ---")
print("Validity Mask:", validity_mask)
print("Valid Scores:", valid_scores)
print("Invalid-value count:", invalid_count)
print("Number of valid scores:", valid_count)

# Part B — Review Flags
review_labels = np.where(valid_scores < 0.80, "review", "accepted")
print("\n--- Part B ---")
print("Review Labels for valid scores:", review_labels)

# Part C — Summary
mean_valid = np.mean(valid_scores)
accepted_count = np.sum(review_labels == "accepted")
review_count = np.sum(review_labels == "review")
share_accepted = accepted_count / valid_count

print("\n--- Part C ---")
print("1. Mean valid confidence:", mean_valid)
print("2. Count marked 'accepted':", accepted_count)
print("3. Count marked 'review':", review_count)
print("4. Share of valid scores marked 'accepted':", share_accepted)