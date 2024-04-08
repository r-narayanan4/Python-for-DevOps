"""
Encapsulation:

Using OOP in Python, we can restrict access to methods and variables.

This prevents data from direct modification, which is called encapsulation.

Whenever you define a variable with __(two underscores i.e. __age), not only the variable but also methods can be restricted in access.

These methods or variables cannot be accessed from outside of a class, but they can be accessed from within the class, from any one of your methods.

This is the way you can hide a variable or method within your class, and this is called encapsulation.

If you use encapsulation for your variables or methods, you can restrict the access of your variables or methods from outside of the class.
"""


class Person(object):
    def assing_name_and_age(self, name, age):
        # Method to assign name and age to the person object
        self.name = name
        self.__age = age  # Private attribute, accessible only within the class
        self.__display()  # Calling private method to display name and age
        return None
    
    def __display(self):
        # Private method to display name and age
        print(self.name, self.__age)
        return None

per1 = Person()  # Creating an instance of Person class

per1.assing_name_and_age('John', 32)  # Assigning name and age to per1 object

# Uncommenting the following lines will raise AttributeError as __display and __age are private
# per1.__display()
# print(per1.__age)
# print(per1.name)
