# Inputs: Test score and threshold values passed explicitly as parameters
# Processing: Demonstrate local vs global scope isolation and pure function evaluation
# Outputs: Compare variable values inside/outside functions and verify qualification checks

# --- Part A: Observe Scope ---
score = 90  # Global variable

def show_score():
    score = 70  # Local variable (shadows global score)
    print("Inside function:", score)

show_score()
print("Outside function:", score)


# --- Part B: Refactor Hidden State ---
def is_qualified(score, threshold):
    """Refactored function receiving threshold explicitly as a parameter."""
    return score >= threshold

# Testing with at least three values as required
print("\n--- Testing Refactored is_qualified Function ---")
print("Score 88, Threshold 85:", is_qualified(88, 85))
print("Score 75, Threshold 80:", is_qualified(75, 80))
print("Score 90, Threshold 95:", is_qualified(90, 95))