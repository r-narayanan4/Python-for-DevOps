class emp:
    count=0  # Class attribute to keep track of the number of employees
    
    def get_emp_details(self, name, age, salary):
        """
        Method to get employee details and display them.
        """
        self.name = name  # Object attribute
        self.age = age    # Object attribute
        self.salary = salary  # Object attribute
        self.increase_count_for_emp()  # Calling method to increase count of employees
        self.display_emp_details()  # Calling method to display employee details
        return None
    
    def increase_count_for_emp(self):
        """
        Method to increase the count of employees.
        """
        emp.count = emp.count + 1  # Class attribute method
        return None
    
    def display_emp_details(self):
        """
        Method to display employee details.
        """
        print(f'The name is: {self.name}\nThe age is: {self.age}\nThe salary is: {self.salary}')
        return None

def main():
    # Creating instances of the emp class (Object instantiation)
    emp1 = emp()  # Object instantiation
    emp2 = emp()  # Object instantiation

    # Getting details for employees
    emp1.get_emp_details('raj', 22, 45000)  # Calling object method
    emp2.get_emp_details('sri', 21, 34400)  # Calling object method

    # Printing the total count of employees (Class attribute)
    print(emp.count)

    # Printing the attributes and methods of the emp class (Class methods)
    #print(dir(emp))

if __name__ == "__main__":
    main()

"""
Class:

Class is a template or blueprint used to create objects in object-oriented programming (OOP). 
It serves as a blueprint for creating instances (objects) that share common attributes and methods.

Attributes:

Attributes are variables associated with a class or its instances. 
They represent the data or characteristics of the objects created from the class. 
Attributes can be defined at both the class level and the object level.

When you define attributes at the class level, they are shared among all instances of the class. 
These are called class attributes.

Methods:

Methods are functions defined within a class that operate on objects created from that class. 
They define the behavior of the class and its instances. Methods can access and modify object attributes.

Usage of 'self':

In Python, 'self' is a convention used to refer to the current instance of the class. 
When defining methods inside a class, the first parameter is always 'self'. 
When calling methods on objects, 'self' is automatically passed and refers to the object itself.

Calling methods:

Inside a class, you call methods using 'self.method_name()'. 
This is how you invoke methods within other methods of the same class. 
Outside the class, you call methods using the object name followed by the method name.

Example of class attribute:

A class attribute is a variable defined directly after the class name. 
It is shared among all instances of the class and is used to store data or information relevant to the entire class.

"""
