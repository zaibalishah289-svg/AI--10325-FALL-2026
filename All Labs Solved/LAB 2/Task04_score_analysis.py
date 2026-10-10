# Input: List of model scores and threshold value
# Processing: Loop through scores, count above/below threshold, calculate average and percentage meeting target
# Output: Detailed model score summary with 2 decimal precision

# Given scores and target threshold
scores = [0.72, 0.81, 0.88, 0.91, 0.67, 0.86, 0.79]
threshold = 0.85

# Reason for placing inside a reusable function:
# Placed in a function so it can evaluate different models or datasets without rewriting the counting and calculation code.

# Check for empty list to prevent ZeroDivisionError
if not scores:
    print("No scores available to analyze.")
else:
    meeting_target = 0
    below_target = 0
    total_score_sum = 0

    # Loop to process each score
    for score in scores:
        total_score_sum += score
        if score >= threshold:
            meeting_target += 1
        else:
            below_target += 1

    total_count = len(scores)
    average_score = total_score_sum / total_count
    percentage_meeting = (meeting_target / total_count) * 100

    # Output formatted clearly with 2 decimal places
    print(f"Meeting target (>= {threshold}): {meeting_target}")
    print(f"Below target: {below_target}")
    print(f"Average score: {average_score:.2f}")
    print(f"Percentage meeting target: {percentage_meeting:.2f}%")