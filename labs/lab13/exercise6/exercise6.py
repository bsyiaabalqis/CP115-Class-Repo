tickets_sold = 0
total_revenue = 0

# TODO: Your code here
while True:
    age = input("Enter your age:")

    age = int(age)

    if age == -1:
        break

    ticket_price = 0
    if age >= 0 and age <= 12:
        ticket_price = 8
    elif age >= 13 and age <= 17:
        ticket_price = 10
    elif age >= 18 and age <= 64: 
        ticket_price = 15
    elif age >= 65:
        ticket_price = 10
    else: 
        print("Invalid age entered. Please enter a positive age or -1 to quit.")
        continue

    tickets_sold += 1
    total_revenue += ticket_price

print(f'Tickets sold: {tickets_sold}')
print(f'Total revenue:{total_revenue}')
