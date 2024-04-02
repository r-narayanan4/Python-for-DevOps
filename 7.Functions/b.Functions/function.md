# Function Concepts

## Defining Functions

Functions are blocks of reusable code that perform a specific task. They allow you to break down your program into smaller, manageable parts.

## Function Calling

Function calling refers to the process of executing or invoking a function to perform its defined task.

## Positional Arguments

Positional arguments are values passed to a function in a specific order, where each value corresponds to a parameter in the function definition.

## Keyword Arguments

Keyword arguments are values passed to a function with the associated parameter name, allowing you to specify arguments out of order.

## Default Arguments

Default arguments are parameters in a function that have preset values, which are used if the caller does not provide a corresponding argument.

## Return Statement in Functions

The return statement is used to exit a function and optionally pass a value or expression back to the caller.
The return keyword is used to exit a function and return a value or expression to the caller. If no value is specified, None is returned.

## Call-by-Value

Call-by-value involves passing a copy of the argument's value to the function. Modifications made to the parameter within the function do not affect the original value.

## Call-by-Reference

Call-by-reference involves passing a reference to the original variable to the function. Changes made to the parameter within the function affect the original value.

- [Understanding Call by Value and Call by Reference](https://www.scaler.com/topics/call-by-value-and-call-by-reference-in-python/): This article provides a detailed explanation of call by value and call by reference in Python. It covers the differences between the two approaches and how they affect variable modification.


## Difference between Call by Value and Call by Reference

| Call by Value                                 | Call by Reference                             |
|-----------------------------------------------|-----------------------------------------------|
| Arguments are copied to the function parameter | Arguments, as well as the formal parameters, refer to the same location |
| Changes made inside the function are not reflected | Changes made inside the function are reflected |
| Immutable Objects are passed in arguments    | Mutable objects are passed in arguments      |

## Defining and Invoking User-Defined Functions and Generators

Creating user-defined functions and generators allows you to encapsulate logic into reusable components.

## The None Keyword

None is a special constant in Python that represents the absence of a value or a null value.

## Recursion

Recursion is a programming technique where a function calls itself in order to solve a problem. It often involves breaking down a problem into smaller instances of the same problem.

## Parameters vs. Arguments

Parameters are variables in a function definition, while arguments are the actual values passed to the function during its invocation.

## Positional, Keyword, and Mixed Argument Passing

Arguments can be passed to functions either positionally, by keyword, or a combination of both.

## Default Parameter Values

Default parameter values are values assigned to parameters in a function definition, which are used when the caller does not provide a corresponding argument.

## Name Scopes and Name Hiding (Shadowing)

Name scopes define where variables can be accessed within a program. Name hiding, or shadowing, occurs when a local variable hides a variable with the same name in an outer scope.

## The Global Keyword

The global keyword is used to declare that a variable is global, allowing it to be accessed and modified from within a function.


