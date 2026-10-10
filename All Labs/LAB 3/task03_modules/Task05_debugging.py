# Inputs: List of test scores
# Processing: Debugged average calculation and corrected conditional classification precedence
# Outputs: Display accurately computed average and correct performance status

def calculate_average(scores):
    if not scores:
        return 0.0
    total = 0
    for score in scores:
        total += score  # FIX: Used += instead of = (which was overwriting total)
    return total / len(scores)

def classify(average):
    if average is None:
        return "No Data"
    # FIX: Reordered conditions so >= 85 is evaluated before >= 50
    elif average >= 85:
        return "Excellent"
    elif average >= 50:
        return "Pass"
    else:
        return "Fail"

# Execution test with given dataset
scores = [60, 70, 80, 90]
average = calculate_average(scores)
result = classify(average)

print(f"Average: {average:.2f}")
print(f"Result: {result}")