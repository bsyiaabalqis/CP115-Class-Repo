# TODO: Your code here
number = 0

for number in range(1, 101):
    print(f'Checking number:{number}')

    if number %7 == 0 and number % 13 == 0:
        found_number = number 
        print(f'Found it! The number is {found_number}')
        break
if found_number:
    print(f'The first number divisible by 7 and 13 is: {found_number}')
else:
    print('No number was found in that range.')
