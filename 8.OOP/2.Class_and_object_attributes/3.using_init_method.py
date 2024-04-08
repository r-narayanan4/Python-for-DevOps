# init_method
class Emp(object):
    def __init__(self, name, salary):
        """
        Constructor method to initialize name and salary attributes of an employee.

        Args:
            name (str): The name of the employee.
            salary (float): The salary of the employee.

        Returns:
            None
        """
        self.name = name
        self.salary = salary
        return None

    def display(self):
        """
        Method to display the name and salary of the employee.

        Returns:
            None
        """
        print(f'The name is: {self.name}\nThe salary is: {self.salary}')
        return None
    
# Creating instances of the Emp class
emp1 = Emp('ramu', 100200)
emp2 = Emp('ravi', 98700)

# Displaying details of emp1 and emp2
emp1.display()
emp2.display()
