'''
Exercise 1 (and Solution)
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old.
 Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year).
'''

name = input("Please enter you name: ")
age = int(input("Please enter your age: "))
year = 100-age+2025
print(f"Hello {name},you will turn 100 years old in " + str(year))
