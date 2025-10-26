grade = float(input())
total = 0
valid_count = 0
average = 0.0

# TODO: Your code here
while grade >0:
    print(f' Processing grade: {grade}')
    valid_count += 1

    if grade < 0 or grade > 100:
        print('Invalid grade, skipping...')
        continue

    total += grade 
    average = total / valid_count
    print(f'Added {grade}. Current total: {average}')

print(valid_count)
print(f"{average:.2f}")
