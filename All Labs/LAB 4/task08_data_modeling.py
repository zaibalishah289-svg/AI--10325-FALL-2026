# Inputs: Architectural data modeling scenarios for AI systems
# Processing: Data structure selection based on mutability, ordering, uniqueness, and key-value mapping
# Outputs: Documented mapping of scenarios to optimal Python data structures

# Task 8: Choose the Right Data Structure Documentation & Demonstration

DATA_STRUCTURE_MAPPING = {
    "Scenario A (Ordered model names)": "list - preserves insertion order and allows sequential indexing.",
    "Scenario B (Fixed image size 224x224)": "tuple - immutable, fixed-size container ideal for coordinates/dimensions.",
    "Scenario C (Model metadata attributes)": "dictionary - maps descriptive string keys to values for structured records.",
    "Scenario D (Unique class labels)": "set - guarantees element uniqueness and optimized membership testing.",
    "Scenario E (Multiple prediction records)": "list of dictionaries - models tabular/collection datasets effectively.",
    "Scenario F (Comparing allowed vs received labels)": "set - enables high-performance set operations like intersection and difference."
}

print("--- Task 8: Data Structure Decisions ---")
for scenario, choice in DATA_STRUCTURE_MAPPING.items():
    print(f"\n{scenario}:\n-> Optimal Choice: {choice}")