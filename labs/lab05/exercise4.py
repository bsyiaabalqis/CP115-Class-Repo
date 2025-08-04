# Basic input and output
print("Welcome to the Shopping Cost Calculator!")
print("This program will calculate your shopping cost.")

# Getting user input (always returns a string)
item_name = input("Enter your item name: ")
item_price = float(input("Enter the item price: "))

# Set fixed variables
quantity = 3
tax_rate = 0.06

# Calculating costs
subtotal = item_price * quantity
tax_amount = subtotal * tax_rate
total_cost = subtotal +  tax_amount


# Display the results
print ("Subtotal:$", subtotal)
print ("Tax Amount:$", tax_amount)
print("Total Cost:$", total_cost)