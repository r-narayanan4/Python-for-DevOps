# Usage_of_constructor

class Emp(object):
    def name_salary(self, name, salary):
        """
        Method to set the name and salary attributes of the employee.

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
emp1 = Emp()
emp2 = Emp()

# Setting attributes for emp1 and emp2
emp1.name_salary('Murali', 5000000)
emp2.name_salary('Narayanan', 9000000)

# Displaying details of emp1 and emp2
emp1.display()
emp2.display()
