target_points = input("Enter target points:")
total = 0 
rounds_played = 0 
total_points = 0

# TODO: Your code here
# Use input() inside the while loop to get points each round
# Custom step pattern 
while True: 
    target_points = int(input("Enter target points:"))
    points = int(input("Enter points:"))
    total+= points
    rounds_played += 1
    total_points = total

    if total>= target_points:
        points = float(input())
        break

print(total_points)
print(rounds_played)