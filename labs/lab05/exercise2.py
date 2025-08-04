# Basic input and output
print("Welcome to the Circle Calculator!")
print("This program will calculate your area and circumference of the circle.")

# Getting user input (always returns a float)
radius = float(input("Enter your radius of the circle: "))


# Importing the math module for mathematical operation 
import math 

# Calculate aarea and circumference
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

# Print the results
print(f"Area of the circle: {area:.2f}")
print(f"Circumference of the circle: {circumference:.2f}")