total = 0
valid_count = 0
average = 0.0

# TODO: Your code here
# Use 'while True' to loop until a sentinel value is encountered
while True:
    grade = float(input("Enter your grade:"))

    # Check for the "stop" condition (sentinel value)
    if grade < 0: 
        print('Invalid grade, skipping...')
        break
        
    # Check for invalid grades to skip    
    if grade > 100:
        print('Invalid grade, skipping...')
        continue

    # Process valid grades
    total += grade 
    valid_count += 1
    print(f'Added {grade}. Current total:{total}')

# Calculate average after each valid grade
if valid_count > 0:  
    average = total / valid_count

print("Valid count: {valid_count}")
print(f"Average:{average:.2f}")
