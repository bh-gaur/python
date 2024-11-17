# def sum(a, b):
#     return a+b

# print(sum(23, 43))

# def summ(a,b):
#     print(a+b)

# summ(434, 4545)


##average of 3 numbers

# def avg(a, b, c):
#     return (a+b+c)/3

# print(avg(98, 97, 95))


#WAF to print the length of a list.
# heroes = ["hulk", "iron man", "superman", "antman", "doctor starnge"]
# def calc_len(list):
#     print(len(list))

# calc_len(heroes)


#WAF to print the elements of a list in a single line.

# movies = [1, 2, 4, 5, 6, 7, 8, 9]
# def list_elements(list):
#     for i in movies:
#         print(i, end=" ")

# list_elements(movies)
# print()


#WAF to find the factorial of n.

# num = 4 
# def calc_factorial(num):
#     factorial = 1
#     for i in range(num, 1, -1):
#         factorial *= i
#     print(factorial)

# calc_factorial(num)

#WAF to convert USD to INR

# USD = 4

# def convert(dollar):
#     INR = 4 * 84.07
#     print(INR)

# convert(USD)



# num = int(input("enter a number: "))

# def checker():
#     num = int(input("enter a number: "))
#     if num%2 == 1:
#         print("ODD")
#     else:
#         print("EVEN")

# checker()

### Recursion

# def show(n):
#     if n==0:
#         return 
#     print(n)
#     show(n-1)

# show(2)

# num = int(input("Enter a number: "))
# def factorial(num):
#     if (num == 0 or num == 1):
#         return 1
#     else:
#         return num * factorial(num-1)
    
# print(factorial(num))


###Calculate sum of n natural numbers using recursion
# num = int(input("Enter a number: "))

# def cal_sum(num):
#     if (num == 0):
#         return 0
#     # elif (num == 1):
#     #     return 1
#     else:
#         return num + cal_sum(num - 1)    
    
# print(cal_sum(5))


### Write a recursive function to print all elements in a list.
##Hint use list and index as parameter
heroes = ["hulk", "iron man", "superman", "antman", "doctor starnge"]

def print_list_elements(list_name, index=0):
    if (index == len(list_name)):
        return
    print(list_name[index])
    print_list_elements(list_name,index+1)

print_list_elements(heroes)