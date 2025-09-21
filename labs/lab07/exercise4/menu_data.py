# import random value 
import random 
from random import choice, shuffle

# create variables
Restaurant_Name = "The Coding Cafe"
Restaurant_location = "123 Code St, Tech City"
Menu_Items = ["Coffee", "Bread", "MilkShake"]

name_upper = Restaurant_Name.upper()
name_lower = Restaurant_Name.lower()
length_location = len(Restaurant_location)

random_choice = choice (['1', '2', '3'])
customer_number = random.randint (100, 999)