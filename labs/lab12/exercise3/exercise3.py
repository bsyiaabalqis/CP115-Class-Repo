age_count = 0
total_age = 0
average_age = 0

while True:
    age_input = input("Enter age or 'done' to finish: ")
    
    if age_input == 'done':
        break
    
    try:
        age = int(age_input)
        total_age += age
        age_count += 1
    except ValueError:
        print("Please enter a valid number or 'done' to finish:")
        continue

if age_count > 0:
    average_age = total_age / age_count

print(f"Count: {age_count}")
print(f"Total: {total_age}")
print(f"Average: {average_age:.2f}")