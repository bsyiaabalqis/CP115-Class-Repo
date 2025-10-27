total = 0
count = 0
cost = 0

price = float(input("Enter the price (or a negative number to stop):")) #prime input

# TODO: Your code here
while price >= 0: #condition
    cost += price
    count += 1
    price = float(input("Enter the price (or a negative number to stop):"))  #update input

item_count = count
total_cost = cost 

print(item_count)
print(f"{total_cost:.2f}")