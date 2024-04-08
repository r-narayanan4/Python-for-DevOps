# Example 1: Simple example illustrating the use of class methods

import datetime

class Person:
    # Define a class variable all_people as an empty list
    all_people = []

    # Define an instance method called __init__ that takes two arguments: name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # Add the instance to the all_people list
        Person.all_people.append(self)

    # Define a class method called from_birth_year that takes two arguments: cls and birth_year
    @classmethod
    def from_birth_year(cls, name, birth_year):
        # Calculate the age based on the current year and birth year
        age = datetime.date.today().year - birth_year
        # Return a new instance of the Person class with the calculated age and given name
        return cls(name, age)

# Create two instances of the Person class
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Create a new instance of the Person class using the class method from_birth_year
person3 = Person.from_birth_year("Charlie", 1990)

# Print the names and ages of all people
for person in Person.all_people:
    print(person.name, person.age)
