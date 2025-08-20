# get input student information from user
name = input ("Enter Student's name:")
studentID = input ("Enter Student's ID:")
age = int(input ("Enter Student's age:"))

# get input course information from user
coursecode = input ("Enter Course code:")
coursename = input ("Enter Course name:")

# import random module and generate two random scores
import random
score1 = random.randint(70-95)
score2 = random.randint(75-100)

# calculate total score by adding the two scores
total_score = score1 + score2 


print(f"Name in UPPERCASE: {name.name_upper}")
print(f"Name in LOWERCASE: {name.name_lower}")
print(f"Name length: {name.name_length} characters")

# import math  module and calculate square root of total score
import math 
square_root = math.sqrt(total_score)
