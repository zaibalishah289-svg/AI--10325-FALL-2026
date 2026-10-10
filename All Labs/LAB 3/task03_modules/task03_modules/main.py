# Main execution script importing functions from score_utils module
from score_utils import calculate_average, is_passing, count_above_threshold

# Given sample dataset
scores = [72, 88, 45, 91, 67]

# Perform required calculations using imported functions
avg = calculate_average(scores)
first_score_passing = is_passing(scores[0])
scores_above_80 = count_above_threshold(scores, 80)

# Display results
print("--- Main Program Execution Output ---")
print(f"Average: {avg:.2f}")
print(f"First score ({scores[0]}) passing: {first_score_passing}")
print(f"Scores at least 80: {scores_above_80}")