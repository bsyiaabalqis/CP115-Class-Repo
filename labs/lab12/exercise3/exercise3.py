age_input = int(input())
age_count = 0 
total_age = 0 
average_age = 0

# TODO: Your code here
while age_input >=1 and age_input <= 120: #condition
    total_age += age_input
    age_count =+ 1
    average_age = total_age / age_count
    age_input = int(input()) #update input

print(age_count)
print(total_age)
print(f"{average_age:.2f}")
