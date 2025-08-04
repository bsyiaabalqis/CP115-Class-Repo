# Basic input and output
print("Welcome to the Average Score Calculator!")

# Getting user input (always returns a string)
test_score_1 = input("Enter the score for Test 1:")
test_score_2 = input("Enter the score for Test 2:")
test_score_3 = input("Enter the score for Test 3:")

# Calculate total score = and average score
total_score = float(test_score_1) + float(test_score_2) + float(test_score_3)
average_score = total_score / 3

# Display scores and average
print (individual_scores := f"Scores: {test_score_1}, {test_score_2},{test_score_3}")
print(f"Total Score: {total_score}")
print(f"Average Score: {average_score:.2f}")