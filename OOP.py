#what is OOP in python
"""
    OOP stands for Object-Oriented Programming. 
    It is a programming paradigm that uses "objects" to represent data and methods to manipulate that data. 
    In Python, OOP allows for the creation of classes, which are blueprints for creating objects.
"""

#what is class and object
"""
    A class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.
    An object is an instance of a class. It is created using the class blueprint and can have its own unique attributes and methods.
"""

######################################################################################
##########    EXAMPLES   ###########################################################
######################################################################################

# class student:      #class
#     name = "karan singh"      #attribute
#     age = 21
#     gender = "male"

# s1 = student()      #object
# print(s1.name)      #calling object ---> karan singh
# print(s1.age)       #calling object ---> 21
# print(s1.gender)    #calling object ---> male

# s2 = student()      #object
# print(s2.name)      #calling object ---> karan singh



###### __init__ Function
## constructor 
'''
    The __init__() function is a special function in Python classes that is automatically called when an object of the class is created. 
    It is used to initialize the object's attributes.
    It is also known as the constructor of the class.
    The syntax is: def __init__(self, arg1, arg2, ...):
    The 'self' parameter refers to the instance of the object being created.
'''

# class student:      #class
#     def __init__(self, name=None, age=None, gender=None):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         print(self)
#         print("'__init__' function is called")

# # initilaize automatically called
# s1 = student()      #object   #'__init__' function is called
# print(s1)


# s2 = student("Bhupender gaur", 21, "male")      #object
# print(s2.name)      #calling object ---> Bhupender gaur
# print(s2.age)       #calling object ---> 21
# print(s2.gender)    #calling object ---> male



# class student:      #class

#     college_name = "IIT Jodhpur"   #class attribute
#     name = "anonymous" #class attribute or variable

#     #default constructor
#     def __init__(self):
#         pass

#     #parameterized constructor
#     def __init__(self, full_name, marks):
#         self.name = full_name      #instance/object attribute > # class attribute
#         self.marks = marks         #instance/object attribute > # class attribute
        
#         print("'adding new student")

# s1 = student("bhupender gaur", 87)    #object
# print(f"{'Name:', s1.name}, {'Marks:', s1.marks}")       #output: bhupender gaur, 87



# #############################
# ######## Methods ######
# '''
#     Methods are functions that belongs to an object
#     it is used to perform operations on the object
# '''

# #creating class
# class Student:
#     def __init__(self, full_name, marks):
#         self.name = full_name
#         self.marks = marks

#     def hello(self):        #self is necessary otherwise error will come
#         print("hello", self.name)

#     def welcome(self):
#         print("welcome to school", self.name)

#     def get_marks(self):
#         return self.marks

#     @staticmethod         #decorator   #static method doesn't take any arguments/ free from class or object
#     def test_static_hello():
#         print("hello students")

    
# #creating object
# s1 = Student("Bhupender gaur", 87)
# s1.hello()
# s1.welcome()
# s1.test_static_hello()
# print(s1.get_marks())






# class Account:
#     def __init__(self, bal, acc_no):
#         self.balance = bal
#         self.account_no = acc_no

#     # debit method
#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs.", amount, "was debited from account")
#         print("total balance is", self.get_balance())

#     # credit method
#     def credit(self, amount):
#         self.balance += amount
#         print("Rs.", amount, "was credited to account")
#         print("total balance is", self.get_balance())

#     def get_balance(self):
#         return self.balance


# acc1 = Account(10000, 76767878)
# # print(acc1.balance)
# # print(acc1.account_no)
# acc1.debit(10001)
# acc1.credit(10000)




###################
## del keyword ##
####################

# class Person:
#     def __init__(self, name):
#         self.name = name

# person1 = Person("Test")
# print(person1.name)

# del person1      # delte the object from memory also we can delete properties directtly by using del object.property
# # print(person1.name)



# ##############################
# # Private(like) attributes and methods
# ## private attributes and methods are meant to be used only within the class and are not accessible from outside the class.


# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.account_no = acc_no
#         self.__acc_pass = acc_pass # putting __ before the variable name makes it private, it is only accessible inside the class

#     def reset_pass(self):
#         print(self.__acc_pass)

# acc1 = Account(133113, "abcdef")
# # print(acc1.account_no)
# acc1.reset_pass()   #this will work
# print(acc1.__acc_pass)


class Account:
    def __init__(self, acc_no=None, acc_pass=None, name="anonymous"):
        self.account_no = acc_no
        self.__acc_pass = acc_pass # putting __ before the variable name makes it private, it is only accessible inside the class
        self.name = name

    def __hello(self):
        print("hello",self.name)

    def welcome(self):
        self.__hello()

acc1 = Account(name="bhupender", acc_no=133113, acc_pass="abcdef")
acc1.welcome()
acc1.__hello()













# class Employee:
    
#     def __init__(self, first_name, last_name, salary):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = f"{first_name.lower()}.{last_name.lower()}@company.com"
#         self.salary = salary

#     def full_name(self):
#         return "{} {}".format(self.first_name, self.last_name)
    
# emp_1 = Employee("John", "Doe", 50000)
# emp_2 = Employee("Jane", "Smith", 60000)
# emp_3 = Employee("test", "user", 70000)

# print(emp_1.email)
# print(emp_2.full_name())
# print(emp_3.full_name())

# print(Employee.full_name(emp_2))

# print(Employee.__dict__)
# print("\n\n", emp_1.__dict__)



# class Dog:
#     # Class Attribute
#     species = "Canis familiaris"

#     # Initializer / Instance Attributes
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     # instance method
#     def description(self):
#         return f"{self.name} is {self.age} years old"

#     # another instance method
#     def speak(self, sound):
#         return f"{self.name} says {sound}"
    
# # Instantiate the Dog object
# mikey = Dog("Mikey", 6)

# # Accessing class attributes and methods
# print(f"{mikey.name} is a {mikey.species}")
# print(mikey.description())
# print(mikey.speak("Woof Woof"))


# class Circle:
#     pass

# Circle_1 = Circle()
# Circle_2 = Circle()

# print(Circle_1)
# print(Circle_2)

# class Employee:          #class definition
    
#     num_of_emps = 0      #class variable
#     raise_amount = 1.05  #class variable

#     def __init__(self, first_name, last_name, salary):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = f"{first_name.lower()}.{last_name.lower()}@company.com"
#         self.salary = salary 

#         Employee.num_of_emps += 1    #incrementing class variable

#     def full_name(self):             #instance method
#         return "{} {}".format(self.first_name, self.last_name)
    
#     def apply_raise(self):
#         self.salary = int(self.salary * self.raise_amount)
    
# emp_1 = Employee("John", "Doe", 50000)
# emp_2 = Employee("Jane", "Smith", 60000)
# emp_3 = Employee("test", "user", 70000)

# print(Employee.num_of_emps)

# emp_1.apply_raise()

# print(emp_1.salary)
# print(emp_2.salary)
# print(emp_3.salary)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# print(emp_3.raise_amount)
# Employee.raise_amount = 1.10    #updating class variable
# print(Employee.raise_amount)
# print(emp_1.raise_amount)








# class Employee:
    
#     num_of_emps = 0      #class variable
#     raise_amount = 1.05  #class variable

#     def __init__(self, first_name, last_name, salary):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = f"{first_name.lower()}.{last_name.lower()}@company.com"
#         self.salary = salary

#         Employee.num_of_emps += 1    #incrementing class variable

#     def full_name(self):
#         return "{} {}".format(self.first_name, self.last_name)
    
#     def apply_raise(self):
#         self.salary = int(self.salary * self.raise_amount)

#     @classmethod
#     def set_raise_amount(cls, amount):
#         cls.raise_amount = amount

#     @classmethod
#     def from_string(cls, emp_str):
#         first, last, salary = emp_str.split("-")
#         return cls(first, last, int(salary))

# emp_str_1 = "John-Doe-50000"
# emp_str_2 = "Jane-Smith-60000"

# emp_1 = Employee.from_string(emp_str_1)
# emp_2 = Employee.from_string(emp_str_2)

# print(emp_1.__dict__)
# print(emp_2.__dict__)

# print(emp_1.email)
# # emp_1 = Employee("John", "Doe", 50000)
# # emp_2 = Employee("test", "user", 70000)

# # print(Employee.raise_amount)
# # print(emp_1.raise_amount)

# # Employee.set_raise_amount(1.11)
# # print(Employee.raise_amount)
# # print(emp_1.raise_amount)








# class Employee:
    
#     num_of_emps = 0      #class variable
#     raise_amount = 1.05  #class variable

#     def __init__(self, first_name, last_name, salary):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = f"{first_name.lower()}.{last_name.lower()}@company.com"
#         self.salary = salary

#         Employee.num_of_emps += 1    #incrementing class variable

#     def full_name(self):
#         return "{} {}".format(self.first_name, self.last_name)
    
#     def apply_raise(self):
#         self.salary = int(self.salary * self.raise_amount)

#     @classmethod
#     def set_raise_amount(cls, amount):
#         cls.raise_amount = amount

#     @classmethod
#     def from_string(cls, emp_str):
#         first, last, salary = emp_str.split("-")
#         return cls(first, last, int(salary))
    
#     @staticmethod # This method is not dependent on any class or instance variable
#     def is_workday(day):
#         if day.weekday() == 5 or day.weekday() == 6:
#             return False
#         return True
    
# import datetime

# my_date = datetime.date(2025, 12, 21)
# print(Employee.is_workday(my_date))  
