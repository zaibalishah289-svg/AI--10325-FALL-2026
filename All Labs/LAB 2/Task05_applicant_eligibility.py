# Input: Applicant age, programming score, and prerequisite completion status
# Processing: Check eligibility against multiple rules and identify any unmet requirements
# Output: Eligibility status and specific unmet requirement messages if applicable

# Sample applicant values (You can change these to test different cases)
age = 19
programming_score = 72
prerequisite_completed = True

print(f"Applicant -> Age: {age}, Score: {programming_score}, Prerequisite: {prerequisite_completed}")

# Check eligibility using separate if statements to catch all failed requirements
is_eligible = True

if age < 18:
    is_eligible = False
if programming_score < 60:
    is_eligible = False
if not prerequisite_completed:
    is_eligible = False

# Print results based on eligibility status
if is_eligible:
    print("Result: Eligible")
else:
    print("Result: Not eligible")
    if age < 18:
        print("- Age requirement not met")
    if programming_score < 60:
        print("- Programming score requirement not met")
    if not prerequisite_completed:
        print("- Prerequisite course not completed")