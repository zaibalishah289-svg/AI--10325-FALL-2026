# Inputs: Initial list of AI experiment accuracy scores
# Processing: List indexing, slicing, mutation, appending, extending, searching, and sorting
# Outputs: Formatted list operations and statistical insights

# Named Constant
THRESHOLD = 0.85

# Given initial dataset
accuracies = [0.82, 0.91, 0.87, 0.78, 0.93, 0.85]

# 1. Print first and last score
print("First:", accuracies[0])
print("Last:", accuracies[-1])

# 2. Print middle four values using slicing
print("Middle four:", accuracies[1:5])

# 3. Add one new score using append()
accuracies.append(0.89)

# 4. Add a batch of two new scores using extend()
accuracies.extend([0.84, 0.90])

# 5. Replace 0.78 with 0.80 using index() (without hard-coding position)
target_val = 0.78
if target_val in accuracies:
    target_index = accuracies.index(target_val)
    accuracies[target_index] = 0.80

# 6. Print updated list
print("Updated:", accuracies)

# 7. Count how many values are >= THRESHOLD
scores_above_threshold = sum(1 for score in accuracies if score >= THRESHOLD)
print(f"Scores >= {THRESHOLD}: {scores_above_threshold}")

# 8. Find highest and lowest scores
print("Highest:", max(accuracies))
print("Lowest:", min(accuracies))

# 9. Print sorted version (high to low) preserving original list
print("Sorted (high to low):", sorted(accuracies, reverse=True))

# 10. Print list again to confirm evaluation order is kept
print("Original order kept:", accuracies)