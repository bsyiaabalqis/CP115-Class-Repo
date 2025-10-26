valid_count = 0
total_withdrawn = 0

# TODO: Your code here
while True: 
    amount = int(input("Enter withdrawal amount:"))
    
    if amount == 0:
        print ("Finishing transactions. Goodbye.")
        break 

    if amount >= 20 and amount <= 500 and amount % 20 == 0:
        print("Withdrawal accepted.")
        valid_count += 1
        total_withdrawn += amount
    else:
        print("Invalid amount, must be multiple of 20. Try again.") 
        continue  

print(valid_count)      # Number of valid withdrawals
print(total_withdrawn)  # Total amount from valid withdrawals only
