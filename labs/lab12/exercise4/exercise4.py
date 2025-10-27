passing_count = 0
failing_count = 0 

print("Enter student scores one by one. Type 'end' when you are finished.")

while True: 
    score_input = input("Enter score (or 'end' to finish):")

    if score_input == "end":
        break

    score = int(score_input)

    if score>= 60:
        print("Pass")
        passing_count += 1 
    else:
        print("Fail")
        failing_count += 1

total_count = passing_count + failing_count

if total_count > 0:
    pass_rate = (passing_count / total_count) * 100
else:
    pass_rate = 0.0

print(f"Total Passing Score: {passing_count}")
print(f"Total Failing Scores: {failing_count}")
print(f"Overall Pass Rate: {pass_rate:.2f}")
