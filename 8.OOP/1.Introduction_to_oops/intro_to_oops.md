# Object-Oriented Programming (OOP) in Python

Python supports both procedural and object-oriented programming concepts.

## What is OOP?

OOP, or Object-Oriented Programming, is all about the use of classes, objects, inheritance, polymorphism, data abstraction, and data encapsulation. In simple terms, OOP is the combination of classes and objects. Objects represent real-world entities and have characteristics (attributes) and functions (methods).

### Objects

An object could be anything that exists in real-time, like humans, fans, cars, emails, applications (e.g., Jenkins, WebLogic, Tomcat, Apache), etc. Each object has characteristics and functions. For example, considering a human or person as an object:

- Characteristics: name, age
- Functions: walking, talking, running

### Why Create Objects?

- **Group Related Functions**: Objects allow grouping related functions (methods) together.
  
- **Template/Blueprint**: Objects serve as templates or blueprints for creating instances with similar characteristics and behaviors.

### Classes

A class is a blueprint for creating objects. Variables in OOP are created dynamically. Inside a class, the `self` keyword is used to refer to the instance itself. Outside the class, object names are used to access class attributes and methods.

### Key Concepts in OOP

- **Encapsulation**: Bundling data and methods within a single unit.
  
- **Inheritance**: Allowing a class (subclass) to inherit properties and behavior from another class (superclass).
  
- **Polymorphism**: The ability of different classes to be treated as instances of the same class through a common interface.

### Methods

When you define a function within a class, it is called a method. The first argument in a method definition is conventionally named `self`, which refers to the instance of the class. Variables defined inside methods should be accessed using `self.variable_name`.

### Creating Objects from Classes

From a class template, you can create any number of objects easily. Each object will have its own set of attributes and methods, inherited from the class.

## Conclusion

OOP allows us to model real-world entities in code by encapsulating their characteristics and behaviors into objects. By organizing related functions into classes, OOP promotes code reusability, modularity, and maintainability.
