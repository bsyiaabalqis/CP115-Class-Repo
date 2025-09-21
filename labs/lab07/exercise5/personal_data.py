import random 
import math 
# get input personal information from user
name = input ("Enter your name:")
age = int(input("Enter your age:")) 
height = float (input("Enter your height in centimeter:"))
weight = float (input("Enter your weight in kilogram:"))
phone_number = input ("Enter your phone number:")
email = input (" Enter your email address:")
street_address = input ("Enter your street address:")
city = input ("Enter your city:")  
postcode = input ("Enter your postcode:")


name_upper = name.upper()
name_lower = name.lower()
length_name = len(name)
city_upper = city.upper()
full_address = f"{street_address}, {city}, {postcode}"
length_full_address = len(full_address)