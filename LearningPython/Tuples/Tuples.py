# day 6 of python -- a tuple is a data structure that is non- mutable 

# empty tuples 
empty_tuple = ()
empty_tuple = tuple()

# tuple with intial values 

tp1 = ('item1','item2','item3')
fruits = ('bananna', 'orange','mango', 'lemon')

# tuple lengths

len(tp1)
len(fruits)

# accessing tuple items 

first_item = tp1[0]
second_item = tp1[1]

first_fruit = fruits[0]
second_fruit = fruits[1]
last_index = len(fruits)-1
last_fruit = fruits[last_index]

# negative indexing 

last_fruit_again = fruits[-1]
second_to_last_fruit = fruits[-2]

# slicing tuples// its basically just litke lists

middle_two_fruits = fruits[1:3]
print(middle_two_fruits)

# changing tuples to lists 



