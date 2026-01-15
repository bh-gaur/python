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

# class Developer(Employee):
#     raise_amount = 1.10  #overriding class variable

#     def __init__(self, first_name, last_name, salary, programming_language):
#         super().__init__(first_name, last_name, salary)
#         # Employee.__init__(self, first_name, last_name, salary)  #alternative way

#         self.programming_language = programming_language

# dev_1 = Developer("John", "Doe", 50000, "Python")
# dev_2 = Developer("Jane", "Smith", 60000, "Java")


# # print(help(Developer))
# # print(dev_1.email)
# # print(dev_2.email)

# print(dev_1.programming_language)
# print(dev_2.programming_language)
# # print(dev_1.salary)
# # dev_1.apply_raise()
# # print(dev_1.salary)

# # print(Employee.raise_amount)









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

class Developer(Employee):         #inherit from Employee
    raise_amount = 1.10  #overriding class variable

    def __init__(self, first_name, last_name, salary, programming_language):
        super().__init__(first_name, last_name, salary)
        # Employee.__init__(self, first_name, last_name, salary)  #alternative way

        self.programming_language = programming_language

class Manager(Employee):         #inherit from Employee
    def __init__(self, first_name, last_name, salary, employees=None):  #default mutable argument avoided
        super().__init__(first_name, last_name, salary)          #initialize parent class
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_employee(self, emp):          #add employee to manager's list
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_employee(self, emp):    #remove employee from manager's list
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_employees(self):           #print all employees under manager
        for emp in self.employees:
            print("-->", emp.full_name())

dev_1 = Developer("John", "Doe", 50000, "Python")
dev_2 = Developer("Jane", "Smith", 60000, "Java")

manager_1 = Manager("Rock", "Johnson", 70000, [dev_1])
print(manager_1.email)

manager_1.add_employee(dev_2)   #add dev_2 to manager_1's list
manager_1.print_employees()

print(isinstance(manager_1, Manager))
print(isinstance(manager_1, Employee))
print(issubclass(Developer, Employee))
print(issubclass(Manager, Developer))
print(issubclass(Manager, Employee))