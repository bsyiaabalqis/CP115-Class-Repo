# import math module
import math 

# Get number from user
number = float(input("Enter a number:"))

# Calculate square root
square_root = math.sqrt(number)
cube_root = number ** (1/3)
sine_value = math.sin(number)

#Display results
print("Square root of", number, "is", square_root)
print("Cube root of" , number, "is", cube_root)
print("Sine value of", number, "is", sine_value)