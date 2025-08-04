# 1. Import the random module
import random

# 2. Get class name from user
class_name = input("Enter your class name: ")

# 3. Generate a random number between 1 and 100
random_number = random.randint(1, 100)

# 4. Display the class information
print("Class Name:", class_name)
print("Random Number for", class_name, "is", random_number)