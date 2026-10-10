# Input: food_expense, transport_expense, other_expense, daily_budget
# Processing: Calculate total, remaining, and evaluate budget status using conditionals
# Output: Total expense, remaining budget, and budget status

# Given values (Whole numbers as specified in guidelines)
food_expense = 450
transport_expense = 200
other_expense = 150
daily_budget = 1000

# Calculate total and remaining budget
total_expense = food_expense + transport_expense + other_expense
remaining_budget = daily_budget - total_expense

# Determine status using if / elif / else
if remaining_budget > 0:
    status = "Within budget"
elif remaining_budget == 0:
    status = "Exactly at budget"
else:
    status = "Over budget"

# Display results clearly (labeled values)
print(f"Total expense: {total_expense}")
print(f"Remaining budget: {remaining_budget}")
print(f"Status: {status}")