# Polymorphism Types

Polymorphism in object-oriented programming refers to the ability of different objects to respond to the same message or method invocation in different ways. There are two main types of polymorphism:

## 1. Compile-time Polymorphism (Static Binding or Early Binding)

- Also known as method overloading or function overloading.
- It occurs when the compiler determines which method or function to invoke at compile time based on the number of arguments and their types.
- The decision is made during compilation and cannot be changed at runtime.
- Examples include:
  - Function overloading in C++.
  - Method overloading in Java and C#.

## 2. Run-time Polymorphism (Dynamic Binding or Late Binding)

- Also known as method overriding.
- It occurs when the method or function to invoke is determined at runtime based on the actual object type.
- The decision is made during program execution and can be changed dynamically.
- Examples include:
  - Method overriding in inheritance in languages like Java, C#, and Python.
  - Virtual functions in C++.

Both types of polymorphism allow for flexibility in programming by enabling different objects to be treated uniformly through a common interface or method signature, while their specific implementations vary based on the object's actual type.
