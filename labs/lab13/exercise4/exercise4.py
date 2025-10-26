positive_sum = 0
positive_count = 0

# TODO: Your code here
while True: 
    number = float(input("Enter your number:"))
    
    if number == 0:
        if positive_count == 0:
            print("Zero is entered, no positive numbers to process.")
        break 

# negative number
    if number <0:
        print("Negative number, skipping...")
        continue

# valid positive number
    if number > 0:
        positive_sum += number
        positive_count += 1

if positive_count > 0:
    print(f"Positive count: {positive_count}")
    print(f"Positive sum:{positive_sum:.2f}")
