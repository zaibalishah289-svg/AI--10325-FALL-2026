# Input: Function definitions with parameters for calculations, pass/fail checks, and counting thresholds
# Processing: Implement reusable logic using return values without internal printing
# Output: Print results of calling each function with sample arguments

def calculate_percentage(obtained, total):
    # Optional check to prevent ZeroDivisionError if total is 0
    if total == 0:
        return 0.0
    return (obtained / total) * 100

def is_passing(score, passing_score):
    return score >= passing_score

def count_values_above_threshold(values, threshold):
    count = 0
    for value in values:
        if value >= threshold:
            count += 1
    return count

# Example calls and expected results matching lab manual:
print(calculate_percentage(423, 500))  # Expected: 84.6
print(is_passing(50, 50))              # Expected: True
print(is_passing(49, 50))              # Expected: False
print(count_values_above_threshold([0.72, 0.81, 0.88, 0.91, 0.67, 0.86, 0.79], 0.85))  # Expected: 3