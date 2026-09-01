'''
Type Hinting:
Type hinting in Python helps make your code easier to understand by showing
what types of values variables and function arguments should have. It can also help
catch errors when using tools like mypy.
'''

# Function that adds two integers and returns an integer
def add(a: int, b: int) -> int:
    return a + b

'''
● a: int and b: int specify that both a and b are integers.
● -> int indicates that the function will return an integer.
'''

# print(add(5, 3))  # Output: 8
# print(type(add(5, 3)))  # Output: <class 'int'>


'''
Command-Line Interfaces (argparse)
The argparse module helps you create programs that can accept input directly from
the terminal (or command line). This is useful when you want your program to be
flexible and run with different options.
'''

import argparse

parser = argparse.ArgumentParser(description="A simple calculator that adds two numbers.")
parser.add_argument("--num1", type=int, help="The first number to add.")
parser.add_argument("--num2", type=int, help="The second number to add.")

args = parser.parse_args()

print(add(args.num1, args.num2))

# command to run the script from the terminal:
# python argument.py --num1 5 --num2 3