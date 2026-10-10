# Inputs: Fixed tuple dimensions, model results, and score sequences
# Processing: Tuple unpacking, returning multiple values as tuples, and dictionary key immutability check
# Outputs: Unpacked fields, score summary tuples, and exception handling demonstration

# --- Part A: Unpacking Fixed Data ---
image_size = (224, 224)
model_result = ("baseline_cnn", 0.91)

# Unpacking tuples into named variables
width, height = image_size
model_name, accuracy = model_result

print("--- Part A: Tuple Unpacking ---")
print(f"Image size: {width} x {height}")
print(f"Model: {model_name} | Accuracy: {accuracy}")


# --- Part B: Returning a Tuple ---
def summarize_scores(scores):
    """Returns (minimum, maximum, average) as a tuple, or None if list is empty."""
    if not scores:
        return None
    min_val = min(scores)
    max_val = max(scores)
    avg_val = sum(scores) / len(scores)
    return min_val, max_val, avg_val


print("\n--- Part B: Summarize Scores Function ---")
test_scores = [72, 88, 91, 67]
summary_result = summarize_scores(test_scores)

if summary_result is not None:
    min_score, max_score, avg_score = summary_result
    print(f"Minimum: {min_score} | Maximum: {max_score} | Average: {avg_score:.1f}")

empty_result = summarize_scores([])
print("Empty:", empty_result)


# --- Part C: Tuples as Dictionary Keys ---
print("\n--- Part C: Tuples as Dictionary Keys ---")
input_models = {
    (224, 224): "resnet50",
    (299, 299): "inception_v3",
    (384, 384): "vit_base"
}

# Lookup for 299 x 299 image
query_dim = (299, 299)
print(f"Model for 299x299: {input_models.get(query_dim)}")

# Attempting to use a mutable list as a dictionary key
try:
    invalid_dict = {[224, 224]: "resnet50"}
except TypeError as e:
    print(f"TypeError: {e}")