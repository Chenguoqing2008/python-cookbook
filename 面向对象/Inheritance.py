#! /usr/bin/python


class Employee:

    raise_amount = 1.04

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def raise_salary(self, amount):
        desc = "{}'s salary is {}, and raise_amount is {} .".format(self.name, self.salary, amount)
        return desc

    @classmethod
    def raise_salary_cls(cls):
        desc = "Employee raise_amount is {} .".format(cls.raise_amount)
        return desc

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, employee_str):
        name, salary = employee_str.split('-')
        return cls(name, salary)

    @staticmethod
    def is_weekday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return True
        else:
            return False


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language


class Manager(Employee):

    def __init__(self, name, salary, emps=None):
        super().__init__(name, salary)
        if emps is None:
            self.emps = []
        else:
            self.emps = emps

    def add_employee(self, employee):
        if employee not in self.emps:
            return self.emps.append(employee)

    def remove_employee(self, employee):
        if employee in self.emps:
            return self.emps.remove(employee)

    def print_employee(self):
        for employee in self.emps:
            print('---->', employee.name)


# inheritance  share the same init method and parent type method
developer = Developer('Rainy', 2100, 'Python')
print(developer.salary)

developer2 = Developer('Sandy', 2500, 'C++')
print(developer2.salary)

# get all the parent code for free
print(help(Developer))

manager = Manager('Jack', 4500, [developer])
manager.print_employee()





