num_rounds = int(input())
final_score = 0.0
rounds_processed = 0

# TODO: Your code here
# Use input() inside the loop to get each round's score
for round in range(num_rounds):
    score=float(input())
    if score > 100:
        bonus = score * 0.20
        final_score += score + bonus
    else: 
        final_score +=score

    rounds_processed +=1
print(f"{final_score:.1f}")
print(rounds_processed)