# Create a class that contains information about employees of a company and define methods to get/set employee name, job title, and start date.

class Company(object):
    """This represents a company in which people work"""

    def __init__(self, name):
        self.name = name
        self.employees = set()

    def get_name(self):
        """Returns the name of the company"""
        def __str__(self):
            return self.name

    def get_employees(self):
        all_employees = ""
        for employee in self.employees:
            all_employees += str(employee) + " , "
        return "Our employees are {}".format(all_employees[0:-1])

class Employee(object):

    def __init__(self, name, title, start_date):
        self.name = name
        self.title = title
        self.start_date = start_date

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name


jimmy_dickens = Employee("Jimmy Dickens", "Emcee", 10201960)
loretta_lynn = Employee("Loretta Lynn", "Lead", 10311960)

opry = Company("Grand Ole Opry")

opry.employees.add(jimmy_dickens)
opry.employees.add(loretta_lynn)

print(opry.get_employees())
print(jimmy_dickens.title)
