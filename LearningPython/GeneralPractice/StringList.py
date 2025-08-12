'''
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
'''

stringy = input("Please enter a string: ")
if stringy=="".join(reversed(stringy)): # i had to research the .join, i only knew the reversed function
    print("this is a palindrome!")
else:
    print("this is NOT a palindrome!")

