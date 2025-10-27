target_points = input("Enter target points:")
total = 0 
rounds_played = 0 

# TODO: Your code here
# Use input() inside the while loop to get points each round
# Custom step pattern 
while total< target_points:
    points = float(input("Enter points:"))
    total+= points
    rounds_played += 1

print(total)
print(rounds_played)