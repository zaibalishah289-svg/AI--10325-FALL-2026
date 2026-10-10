# Inputs: Raw numerical scores, student mappings, and capitalization-variant classification labels
# Processing: List, dictionary, and set comprehensions for filtering, transformation, and normalization
# Outputs: Cleaned scores, normalized floats, pass/fail status dicts, and unique lowercase label sets

# --- Part A: List Comprehension ---
print("--- Part A: List Comprehension ---")
raw_scores = [78, -5, 92, 110, 67, 85]

# Filter valid scores (0 <= score <= 100)
valid_scores = [score for score in raw_scores if 0 <= score <= 100]
print("Valid:", valid_scores)

# Create normalized scores list (score / 100)
normalized_scores = [score / 100 for score in valid_scores]
print("Normalized:", normalized_scores)


# --- Part B: Dictionary Comprehension ---
print("\n--- Part B: Dictionary Comprehension ---")
student_scores = {
    "Ali": 72,
    "Sara": 91,
    "Ahmed": 45,
    "Fatima": 88
}

# Create pass_status mapping student names to True/False based on passing grade (>= 50)
pass_status = {name: score >= 50 for name, score in student_scores.items()}
print("Pass status:", pass_status)


# --- Part C: Set Comprehension ---
print("\n--- Part C: Set Comprehension ---")
labels = ["Spam", "HAM", "spam", "Ham", "UNKNOWN"]

# Create a set containing normalized lowercase labels
normalized_labels = {label.lower() for label in labels}
print("Labels:", sorted(normalized_labels))