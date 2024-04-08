# Example 2: Employee class using class methods

class Employee:
    raise_amount = 1.05  # class variable

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount  # class method to set raise amount

# Create instances of the Employee class
emp1 = Employee("John", "Doe", 50000)
emp2 = Employee("Jane", "Smith", 60000)

# Print the initial raise amount
print(Employee.raise_amount)

# Call the class method to set raise amount to 1.10
Employee.set_raise_amount(1.10)

# Print the updated raise amount
print(Employee.raise_amount)
