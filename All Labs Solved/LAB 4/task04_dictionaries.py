# Inputs: Raw metadata and attributes of an AI model
# Processing: Dictionary creation, record updating, safe retrieval with .get(), iteration, and nested dictionaries
# Outputs: Structured model details, safe defaults, and nested metric extraction

# --- Part A: Basic Dictionary Operations & Structured Records ---
print("--- Part A: Model Record Dictionary ---")
model_record = {
    "name": "spam_classifier",
    "version": 2,
    "accuracy": 0.92,
    "threshold": 0.80,
    "status": "evaluated"
}

# 2. Print model name
print("Model Name:", model_record["name"])

# 3. Update accuracy to 0.94
model_record["accuracy"] = 0.94

# 4. Add owner field
model_record["owner"] = "AI-216 Team"

# 5. Read a missing field using .get() with a sensible default
framework = model_record.get("framework", "scikit-learn")
print("Framework (Default):", framework)

# 6. Iterate through all key-value pairs
print("\nAll Model Attributes:")
for key, value in model_record.items():
    print(f"- {key}: {value}")


# --- Part B: Nested Dictionary ---
print("\n--- Part B: Nested Metrics Dictionary ---")
# Adding nested performance metrics
model_record["metrics"] = {
    "accuracy": 0.94,
    "precision": 0.91,
    "recall": 0.89
}

# Print only precision and recall without printing the whole dictionary
print("Precision:", model_record["metrics"]["precision"])
print("Recall:", model_record["metrics"]["recall"])