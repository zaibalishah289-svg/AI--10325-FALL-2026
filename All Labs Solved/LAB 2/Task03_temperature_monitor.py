# Input: A list of temperature readings
# Processing: Loop through temperatures, classify each using conditional rules, and count occurrences
# Output: Category for each temperature and final summary counts

# Given temperature readings
temperatures = [21.5, 29.0, 32.5, 18.0, 35.2, 27.8, 14.0]

# Initialize counters for each category
below_normal_count = 0
normal_count = 0
high_count = 0

# Loop through each temperature in the list
for temp in temperatures:
    if temp < 15:
        print(f"Temperature {temp}°C: Below Normal")
        below_normal_count += 1
    elif 15 <= temp <= 30:
        print(f"Temperature {temp}°C: Normal")
        normal_count += 1
    else:
        print(f"Temperature {temp}°C: High")
        high_count += 1

# Print final summary counts
print("\n--- Final Summary ---")
print(f"Below Normal: {below_normal_count}")
print(f"Normal: {normal_count}")
print(f"High: {high_count}")