# Data Abstraction

Abstraction is an important aspect of object-oriented programming. It is used to hide the internal functionality of functions from users. Users interact only with the basic implementation of the function, while the inner workings remain hidden. Users know what a function does, but not necessarily how it accomplishes it. 

For example, when increasing the volume on a TV, users only need to press the '+' button without knowing the details of volume adjustment.

In Python, data hiding can be achieved by adding a double underscore (__) as a prefix to the attribute that needs to be hidden. After this, the attribute will not be visible outside of the class through the object.

Data abstraction, which involves showing only the necessary details while hiding the complexity of the program implementation, is not supported by default in Python.

**Data abstraction** - showing only the necessary details by hiding the complexity of the program implementation.

Abstract methods are declared without a definition. To create a method in an abstract class, you need to use the `@abstractmethod` decorator.

An abstract class must have at least one abstract method. Objects cannot be created using an abstract class.

## Why we need abstract class and abstract method ?

In a large project, it's essential to maintain consistency and enforce a standardized structure across classes. Abstract classes and abstract methods serve as blueprints, ensuring that every subclass adheres to certain rules and guidelines.

For instance, consider a scenario where multiple classes have a method responsible for starting their respective vehicles. Without a defined rule, each class might name this method differently, leading to confusion and inconsistency. By implementing an abstract class with an abstract method named 'start', we enforce a uniform structure across subclasses.

In the provided example:

```Python

from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, n):
        self.no_of_tyres = n

    @abstractmethod
    def start(self):
        pass

    def display(self):
        print("Hi, I am calling from the vehicle class.")

class Bike(Vehicle):
    def __init__(self, n, color):
        super().__init__(n)
        self.color = color

    def start(self):
        print("Start with Kick")

    def display(self):
        print(f"My color is {self.color}")

class Scooty(Vehicle):
    def start(self):
        print("Self start")

class Car(Vehicle):
    def __init__(self, n, no_of_gears):
        super().__init__(n)
        self.no_of_gears = no_of_gears

    def start(self):
        print("Start with key")
```

We see how each subclass (Bike, Scooty, and Car) implements the start method according to its specific functionality. This ensures consistency and clarity throughout the project, making it easier to maintain and understand.
