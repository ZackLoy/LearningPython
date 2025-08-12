'''
The exercise comes first (with a few extras if you want the extra challenge or want to spend more time), 
followed by a discussion. Enjoy!

Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 
Hint: how does an even / odd number react differently when divided by 2?
'''

num = float(input("Enter a number: "))

if num%2==0 and num%4==0:
    print("the number is even and a multiple of 4!")
elif num%2==0:
    print("the number is even!")
else:
    print("the number is odd and not a multiple of 4!")
    