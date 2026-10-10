# Inputs: Obtained marks and total marks
# Processing: Validate rules using raise ValueError and process input using try-except-else-finally blocks
# Outputs: Display calculated percentage or descriptive error message

def calculate_percentage(obtained, total):
    if total <= 0:
        raise ValueError("Total marks must be strictly greater than 0.")
    if obtained < 0:
        raise ValueError("Obtained marks cannot be negative.")
    if obtained > total:
        raise ValueError("Obtained marks cannot be greater than total marks.")
    
    return (obtained / total) * 100


def test_calculator(obtained_input, total_input):
    print(f"\n--- Testing with obtained={obtained_input}, total={total_input} ---")
    try:
        # Convert inputs to float to handle potential type/conversion errors
        obtained = float(obtained_input)
        total = float(total_input)
        
        result = calculate_percentage(obtained, total)
    except ValueError as error:
        print("Error caught:", error)
    else:
        print(f"Success! Calculated Percentage: {result:.2f}%")
    finally:
        print("Validation check completed.")


# Required Test Cases
test_cases = [
    (80, 100),       # Valid case
    (-5, 100),       # Negative obtained
    (120, 100),      # Obtained > total
    (80, 0),         # Total <= 0
    ("eighty", 100)  # Non-numeric input
]

for ob, tot in test_cases:
    test_calculator(ob, tot)