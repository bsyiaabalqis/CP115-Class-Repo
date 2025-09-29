current_reading = int(input())
previous_reading = int(input())

# TODO: Your code here
consumption = current_reading - previous_reading 
if consumption <= 20: 
    water_cost = consumption * 0.57
elif consumption > 20 and current_reading <= 35:
    water_cost = (consumption * 1.03) + (20 * 0.57)
else:
    water_cost = (consumption * 1.40) + (20 * 0.57) + (15 * 1.03)
    
total_bill = water_cost + 8 + 2 

print(consumption)
print(water_cost)
print(total_bill)