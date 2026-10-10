# Inputs: Experiment accuracy scores, model predictions, and ground truth labels
# Processing: Iteration with enumerate() using custom start index, and parallel iteration using zip() for evaluation
# Outputs: Numbered experiment logs, prediction comparisons, and calculated accuracy metrics

# --- Part A: enumerate() ---
print("--- Part A: enumerate() ---")
experiments = [0.81, 0.86, 0.79, 0.91]

# Print experiments with 1-based indexing
for idx, score in enumerate(experiments, start=1):
    print(f"Experiment {idx}: {score}")


# --- Part B: zip() ---
print("\n--- Part B: zip() Evaluation ---")
predictions = [True, False, True, True]
actual = [True, False, False, True]

correct_count = 0
total_predictions = len(predictions)

# Compare each predicted value with the actual value using zip()
for pred, act in zip(predictions, actual):
    is_correct = (pred == act)
    if is_correct:
        correct_count += 1
    print(f"Predicted: {pred} | Actual: {act} | Correct: {is_correct}")

# Calculate and print final accuracy
accuracy = correct_count / total_predictions
print(f"Final Accuracy: {accuracy * 100:.1f}%")