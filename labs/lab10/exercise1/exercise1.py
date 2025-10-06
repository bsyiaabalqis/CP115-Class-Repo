position = input()
overtime_hours = int(input())
is_weekend = input()

# Determine base hourly rate based on position
if position == "Manager":
    hourly_rate = 35
elif position == "Supervisor":
    hourly_rate = 25
elif position == "Staff":
    hourly_rate = 18
else: 
    hourly_rate = 0

# Calculate the base overtime pay (without the bonus)
total_pay =(hourly_rate * 1.5) * overtime_hours

# Calculate the weekend bonus separate;y and add it to the total
if is_weekend.lower()== 'yes' :
    weekend_bonus = 5 * overtime_hours
    total_pay += weekend_bonus 

   
print(hourly_rate)
print(total_pay)