# Day2: 30 Days of Python Programming
import math
# declaring variables 
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name +" "+ last_name
country = input("Enter your country: ")
city = 'New Martinsville'
age = input("Enter your age: ")
year = '2025'
is_married = False
is_true = True
is_light = False
x, y, z = True, 18, "Last"

# checking the type 
print(type(first_name)) 
print(type(last_name))
print(type(full_name)) 
print(type(country))
print(type(city)) 
print(type(age)) 
print(type(year))
print(type(is_married)) 
print(type(is_true)) 
print(type(is_light)) 
print(type(x))
print(type(y))
print(type(z))
# checking length and comparing
print(len(first_name))
print(first_name>last_name)

num_one = 5
num_two = 4
# math operations
total = num_one+num_two
diff = num_one-num_two
product = num_one*num_two
division = num_one / num_two
remainder = num_two%num_one
exp = num_one**num_two
floor_divsion = num_one//num_two

# area of a circle w/ radius 30m
# using the math import for a more exact pi
radius = float(input("Enter a non-negative value: "))
area_of_circle = math.pi*(radius**2)
circum_of_circle = 2*math.pi*radius 

help('keywords')
