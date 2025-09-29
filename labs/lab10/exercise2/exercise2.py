age = int(input())
accident_count = int(input())

# Determine base premium by age
if age < 25:
    base_premium = 2400
elif age>= 25 or age <=50:
    base_premium = 1800
elif age >= 50:
    base_premium = 2000
else :
    base_premium = 0 

# Accident penalty calculation
if accident_count == 0:
    accident_penalty = 0
elif accident_count >= 1 and accident_count <= 2:
    accident_penalty =300 
elif accident_count >= 3:
    accident_penalty = 600
else: 
    accident_penalty = 0

# good driver discount
discount_amount = 0 
if accident_count == 0:
    discount_amount = (base_premium + accident_penalty) * 0.10

final_premium = base_premium + accident_penalty - discount_amount     

print(base_premium)
print(final_premium)
print(discount_amount)