# ask ticket_price and age from user
ticket_price = float(input("Enter your ticket price:"))
age = int(input("Enter your age:")) 
#check if ticket_price is not negative
if ticket_price < 0:    
    print("Invalid input. Please enter a number")
#check if age is not negative
elif age < 0:       
        print ("Error: Age cannot be negative.")
elif age <= 12:
        print("Category: Children")
        discount = 0.50
elif age <= 17: 
        print("Category: Teenagers")
        discount = 0.25
else: 
        print("Category: Adults")
        discount = 0.0
# calculate final price after discount
if ticket_price >=0 and age >= 0:
        final_price = ticket_price - (ticket_price * discount)
        print(f"Final ticket price after discount:RM{final_price:.2f}")
