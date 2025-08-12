# day 5 of 30 days of python

# there are 4 data types in python:
# List - mutable and ordered []
# Tuple - non- mutable and ordered 
# Set - unordered and mutable
# Dictionary - unordered buy key value pairs

empty_list = [] # creates empty list
listOfSix = ['apple','green apple','blue apple','green apple','purple apple','white apple'] # creates list of 6
print(len(listOfSix)) # 6

#print(listOfSix[0]) # first item
#print(listOfSix[-1]) # last item
#print(listOfSix[int(len(listOfSix)/2)]) # middle item

mixed_data = ['Zack','18','5.833',"Non- Married","125 Central St"]
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
print(it_companies)
print(len(it_companies))
print(it_companies[0]," ",it_companies[-1])
it_companies[1] = 'Youtube'
print(it_companies)
