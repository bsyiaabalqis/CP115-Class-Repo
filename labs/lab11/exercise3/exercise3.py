target_points = int(input())
total = 0 
rounds_played = 0 
total_points = 0

# TODO: Your code here
# Use input() inside the while loop to get points each round
# Custom step pattern 
while total>= target_points:
    points = float(input())
    total += points
    rounds_played +=1
    total_points = total

print(total_points)
print(rounds_played)