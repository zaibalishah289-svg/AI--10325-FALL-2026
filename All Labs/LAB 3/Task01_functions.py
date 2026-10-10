# Inputs: List of student assessment scores
# Processing: Reusable functions for average, maximum, threshold count, and performance classification
# Outputs: Formatted summary of score metrics

scores = [78, 85, 92, 67, 88]
threshold = 80

def calculate_average(scores):
    if not scores:
        return None
    return sum(scores) / len(scores)

def find_highest(scores):
    if not scores:
        return None
    return max(scores)

def count_above_threshold(scores, threshold):
    count = 0
    for score in scores:
        if score >= threshold:
            count += 1
    return count

def classify_average(average):
    if average is None:
        return "No valid data"
    elif average >= 85:
        return "Excellent"
    elif 70 <= average < 85:
        return "Good"
    elif 50 <= average < 70:
        return "Satisfactory"
    else:
        return "Needs Improvement"

# Execution & Display
avg = calculate_average(scores)
highest = find_highest(scores)
above_threshold_count = count_above_threshold(scores, threshold)
classification = classify_average(avg)

print(f"Scores: {scores}")
print(f"Average: {avg:.2f}" if avg is not None else "Average: None")
print(f"Highest Score: {highest}")
print(f"Scores >= {threshold}: {above_threshold_count}")
print(f"Performance Classification: {classification}")