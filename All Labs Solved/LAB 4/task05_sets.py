# Inputs: Training and test classification label collections
# Processing: Set conversion, union (|), intersection (&), and difference (-) set operations
# Outputs: Unique labels, shared labels, unseen labels, and combined vocabulary sets

# Given datasets
training_labels = ["spam", "ham", "spam", "promotion", "ham"]
test_labels = ["spam", "ham", "unknown", "promotion"]

# 1. Convert both collections into sets
train_set = set(training_labels)
test_set = set(test_labels)

# 2. Print unique training labels (sorted for predictability)
print("Unique training labels:", sorted(train_set))

# 3. Print labels present in both datasets (Intersection)
common_labels = train_set & test_set
print("In both:", sorted(common_labels))

# 4. Print labels present in test set but not in training set (Difference)
unseen_labels = test_set - train_set
print("Only in test:", sorted(unseen_labels))

# 5. Print labels present in either dataset (Union)
all_labels = train_set | test_set
print("In either:", sorted(all_labels))