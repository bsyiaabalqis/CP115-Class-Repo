score1 = float(85) 
score2 = int(92.5)
score3 = int(78)

average_score1 = int(score1 + score2 + score3) / 3
average_score2 = int(score1 ** 2 / score2 + score3 % 7)

print(f"average_score1 = {average_score1} (type: {type(int(average_score1))}")
print(f"average_score2 = {average_score2} (type: {type(average_score2)})")
