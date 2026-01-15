class Employee:
    
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.email = f"{first_name.lower()}.{last_name.lower()}@company.com"
        self.salary = salary

    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)
    
    def __repr__(self):             #official string representation
        return "Employee('{}', '{}', {})".format(self.first_name, self.last_name, self.salary)
    
    def __str__(self):              #informal string representation
        return "{} - {}".format(self.full_name(), self.email)
    
    def __add__(self, other):        #operator overloading
        return self.salary + other.salary
    
    def __len__(self):              #len() method overloading
        return len(self.full_name())
    

emp_1 = Employee("John", "Doe", 50000)
emp_2 = Employee("Jane", "Smith", 60000)
emp_3 = Employee("test", "user", 70000)

# print(emp_1)  #outputs: <__main__.Employee object at 0x7d53361942e0>  with default __str__ and __repr__ methods

# print(repr(emp_1))

# print(str(emp_1))
# print(emp_1.__repr__())
# print(emp_1.__str__())

# print(emp_1)

# print(emp_1 + emp_2)  #outputs: 110000

print(len(emp_1))      #outputs: 8
