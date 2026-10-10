# Problem: Classify daily electricity usage into Low, Normal, or High categories and calculate counts and percentages.
# Inputs: daily_usage_kwh list
# Rules: Low < 5, Normal 5 <= usage <= 10, High > 10
# Repetition: for loop iterating through each daily usage value in the list
# Outputs: Category counts and formatted percentages (with 2 decimal places)

# Given daily usage data in kWh
daily_usage_kwh = [3.2, 5.0, 7.5, 10.0, 12.4, 4.9, 10.1]

# Initialize counters
low_count = 0
normal_count = 0
high_count = 0

# Loop through each reading and classify
for usage in daily_usage_kwh:
    if usage < 5:
        low_count += 1
    elif 5 <= usage <= 10:
        normal_count += 1
    else:
        high_count += 1

# Calculate percentages
total_days = len(daily_usage_kwh)

if total_days > 0:
    low_percentage = (low_count / total_days) * 100
    normal_percentage = (normal_count / total_days) * 100
    high_percentage = (high_count / total_days) * 100
else:
    low_percentage = normal_percentage = high_percentage = 0.0

# Print expected summary with 2 decimal places
print(f"Low: {low_count} ({low_percentage:.2f}%)")
print(f"Normal: {normal_count} ({normal_percentage:.2f}%)")
print(f"High: {high_count} ({high_percentage:.2f}%)")