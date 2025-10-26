# Using break - stops when found
for number in range(10):
    if number <= 7:
        continue # Skip numbers <= 7
    print(f'Number greater than 7: {number}') # Reports 8 and 9 

print('Processing complete')