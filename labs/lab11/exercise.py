# The smart way - let Python count for you
print("Printing 5 receipts:")
for receipt_number in range(5):
    print(f"Receipt #{receipt_number + 1} printed")

# Single parameter: range(stop)
print("Basic range counting:")
for count in range(4):
    print(f"Count: {count}")

# Two parameters: range(start, stop)
print("Custom start and stop:")
for number in range(10, 15):
    print(f"Number: {number}")

# Three parameters: range(start, stop, step)
print("Counting by 3s:")
for value in range(0, 12, 3):
    print(f"Value: {value}")

# Counting by 5s
print("Counting by 5s:")
for value in range(0, 25, 5):
    print(f"Value: {value}")

# Count determined by user input
team_size = int(input("How many team members? "))
print(f"Registering {team_size} team members:")

for member in range(1, team_size + 1):
    name = input(f"Enter name for member {member}: ")
    print(f"Member {member}: {name} registered")

print("Team registration complete!")

# Count from calculation
months_in_year = 12
years = 3
total_months = months_in_year * years

print(f"Monthly report for {years} years:")
for month in range(1, total_months + 1):
    year_number = (month - 1) // 12 + 1
    month_in_year = (month - 1) % 12 + 1
    print(f"Month {month}: Year {year_number}, Month {month_in_year}")

# Counter used in calculations
print("Multiplication table for 7:")
for multiplier in range(1, 11):
    result = 7 * multiplier
    print(f"7 x {multiplier} = {result}")

# Basic while loop counter pattern
attempt = 1                    # Step 1: Initialize
while attempt <= 3:            # Step 2: Condition
    print(f"Attempt number: {attempt}")
    attempt += 1               # Step 3: Update