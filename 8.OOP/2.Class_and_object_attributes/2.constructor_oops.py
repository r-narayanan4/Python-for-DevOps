class Emp:
    count = 0  # Class variable to count the number of objects created
    
    def __init__(self):
        """
        Constructor method to increment the count of objects created from Emp class.

        Args:
            None

        Returns:
            None
        """
        Emp.count += 1
        return None

    def display(self):
        """
        Method to display a message.

        Returns:
            None
        """
        print("This is a display method")
        return None

# Creating instances of the Emp class
emp1 = Emp()
emp2 = Emp()

# Printing the number of objects created from Emp class
print('The number of objects created from Emp class are: ', Emp.count)


"""
Concept of Constructor of a class

Constructor is a special method in a class, and it is called by default whenever you create an object from a class.

We know that a class is nothing but a combination of attributes and methods, and if you want to execute any method from your class, you always need to call it from your object.

But if you define a constructor method instead of a class, you don't need to call it explicitly. By default, it will execute whenever you create an object.

def __init__():

This will be called by default whenever you create an object. This is the initialization method.
"""
