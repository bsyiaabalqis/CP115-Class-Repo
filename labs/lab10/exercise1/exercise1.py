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

# Calculate the overtime pay per hour
overtime_rate_per_hour = hourly_rate * 1.5

# Add the weekend bonus if applicable
if is_weekend.lower() == 'yes':
    overtime_rate_per_hour += 5

# Calculate the total overtime pay
overtime_pay = overtime_rate_per_hour * overtime_hours

# The total pay is the overtime pay, assuming no regular hours are being calculated here
total_pay = overtime_pay
   
print(hourly_rate)
print(overtime_pay)
print(total_pay)