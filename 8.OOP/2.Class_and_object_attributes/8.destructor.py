# The concept of a destructor in Python revolves around the automatic memory management system, also known as garbage collection.
# Python employs a garbage collector to automatically free up memory occupied by objects that are no longer in use.

# A destructor is a method within a class that is automatically called when an object is destroyed or deleted.
# In Python, the __del__() method serves as the destructor, and it is invoked when the reference count of an object reaches zero,
# indicating that there are no more references to the object.

# However, it's important to note that Python's garbage collector handles memory management automatically,
# so developers typically do not need to explicitly define a destructor method.
# The garbage collector automatically deallocates memory for objects that are no longer reachable.

# Here's a basic example illustrating the concept of a destructor in Python:

class Person:
    def __init__(self, name, age):
        print("An object has been created")
        self.name = name
        self.age = age

    def __del__(self):
        print("Object has been deleted")

# Creating an instance of the Person class
per1 = Person('John', 23)

# The object per1 will be automatically deleted when it goes out of scope and there are no more references to it.
# Upon deletion, the __del__() method is invoked, printing "Object has been deleted".
# However, in practice, developers rarely need to explicitly define the __del__() method for basic memory management tasks.
