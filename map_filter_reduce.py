
###############################
##### lambda function in python #####
###############################

# add_lambda = lambda a, b: a+b
# print(add_lambda(23, 43))



#############
## map() function in python

# Map: Applies a function to all items in an input list.
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared) # Output: [1, 4, 9, 16]



#################
## filter() function in python

# Filter: Filters elements based on a condition.
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers) # Output: [2, 4]



#################
## reduce() function in python

# Reduce (from functools): Reduces a list to a single value by applying a function cumulatively.
from functools import reduce
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product) # Output: 24