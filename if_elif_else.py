# #Calculator

# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# def multiply(x, y):
#     return x * y

# def divide(x, y):
#     if y == 0:
#         return "Error! Division by zero."
#     else:
#         return x / y

# def calculator():
#     print("Select operation:")
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")

#     choice = input("Enter choice (1/2/3/4): ")

#     if choice in ['1', '2', '3', '4']:
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))

#         if choice == '1':
#             print(f"{num1} + {num2} = {add(num1, num2)}")

#         elif choice == '2':
#             print(f"{num1} - {num2} = {subtract(num1, num2)}")

#         elif choice == '3':
#             print(f"{num1} * {num2} = {multiply(num1, num2)}")

#         elif choice == '4':
#             print(f"{num1} / {num2} = {divide(num1, num2)}")

#     else:
#         print("Invalid input")


# # Start the calculator
# if __name__ == "__main__":
#     calculator()


         ###check number is even or odd
# num = int(input("enter a number: "))

# if(num%2 == 0):
#     print("number is even")
# elif(num%2 == 1):
#     print("number is odd")

# new = num % 2
# if(new == 0):
#     print("EVEN")
# else:
#     print("ODD")

         ###WAP to find greatest of 4 numbers entered by user

# a = int(input("enter first number: "))
# b = int(input("enter second number: "))
# c = int(input("enter third number: "))
# d = int(input("enter fourth number: "))

# if(a>=b and a>=c and a>=d):
#     print("first number is largest:",a)
# elif(b>=c and b>=d):
#     print("second number is largest:",b)
# elif(c>=d):
#     print("third number is largest:",c)
# else:
#     print("fourth number is largest:",d)


            ###WAP to program to check if number is a multiple of 7 or not

# number = int(input("enter a number: "))

# next = number % 7

# if(next == 0):
#     print("given number is multiple of seven")
# else:
#     print("given number is not multiple of seven")