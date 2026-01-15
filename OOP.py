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








class Employee:
    
    num_of_emps = 0      #class variable
    raise_amount = 1.05  #class variable

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.email = f"{first_name.lower()}.{last_name.lower()}@company.com"
        self.salary = salary

        Employee.num_of_emps += 1    #incrementing class variable

    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)
    
    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, salary = emp_str.split("-")
        return cls(first, last, int(salary))
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    
import datetime

my_date = datetime.date(2025, 12, 21)
print(Employee.is_workday(my_date))  