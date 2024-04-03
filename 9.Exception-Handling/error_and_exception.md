# Python Error Handling: `try`, `except`, `else`, `finally`

Error handling is a crucial aspect of writing robust Python programs. Python provides the `try`, `except`, `else`, and `finally` blocks to handle exceptions gracefully.

## `try` Block

The `try` block allows you to test a block of code for errors. If an error occurs within the `try` block, Python stops executing the `try` block and jumps to the `except` block.

```python
try:
    # Code block that might raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    # Handling the specific exception
    print("Division by zero is not allowed!")
```

## `except` Block

The `except` block catches and handles the exception raised within the try block. You can specify which type of exception you want to catch.

```python
try:
    # Code block that might raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    # Handling the specific exception
    print("Division by zero is not allowed!")
except:
    # Handling any other exceptions
    print("An error occurred!")
```

## `else` Block

The `else` block is executed if no exceptions are raised in the `try` block. It is optional.

```python

try:
    # Code block that might raise an exception
    result = 10 / 2  # This will not raise any exception
except ZeroDivisionError:
    # Handling the specific exception
    print("Division by zero is not allowed!")
else:
    # Code to execute if no exception occurred
    print("Division successful. Result:", result)
```

## `finally` Block

The `finally` block allows you to execute code, regardless of whether an exception occurred or not. It is executed irrespective of whether an exception is raised or not.

```Python

try:
    # Code block that might raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    # Handling the specific exception
    print("Division by zero is not allowed!")
finally:
    # Code to execute whether an exception occurred or not
    print("This will always execute, regardless of exceptions.")
```

## Basics of Python Exception Handling

## try-except / the try-except Exception

In Python, the `try-except` block is used to handle exceptions. Code that might raise an exception is placed inside the `try` block, and the corresponding exception handling code is placed inside the `except` block.

## Ordering the except branches

When handling multiple exceptions in Python, it's important to order the `except` branches correctly. More specific exceptions should be placed before more general ones to ensure that the correct exception is caught and handled.

## Propagating exceptions through function boundaries

Exceptions can be propagated through function boundaries using the `raise` statement. When an exception is raised within a function, it can be caught and handled by higher-level code, allowing for more centralized error handling.

## Delegating responsibility for handling exceptions

In Python, responsibility for handling exceptions can be delegated to higher-level code by re-raising exceptions using the `raise` statement. This allows exceptions to be handled at a more appropriate level in the code hierarchy, leading to cleaner and more maintainable code.

## About Custom Exceptions

Custom exceptions in Python allow developers to create their own exception classes tailored to specific application needs. This can provide more meaningful error messages and allow for more precise error handling in the code. Custom exceptions are typically defined by creating a new class that inherits from the built-in `Exception` class or one of its subclasses. They can include additional attributes and methods to provide more information about the error and how to handle it.


## Python Built-In Exceptions Hierarchy

## BaseException

`BaseException` is the base class for all built-in exceptions in Python. It provides the root of the exception hierarchy.

## Exception

`Exception` is a subclass of `BaseException` and serves as a base class for most built-in exceptions. It is typically used for user-defined exceptions as well.

## SystemExit

`SystemExit` is raised by the `sys.exit()` function to exit the Python interpreter.

## KeyboardInterrupt

`KeyboardInterrupt` is raised when the user interrupts the execution of a program, typically by pressing Ctrl+C.

## Abstract Exceptions

Abstract exceptions are not meant to be directly instantiated. They serve as base classes for other exceptions in the hierarchy.

## ArithmeticError

`ArithmeticError` serves as a base class for exceptions that occur during arithmetic operations, such as `ZeroDivisionError`.

## LookupError

`LookupError` serves as a base class for exceptions that occur when a key or index is not found in a collection.

## IndexError

`IndexError` is raised when a sequence subscript is out of range.

## KeyError

`KeyError` is raised when a dictionary key is not found in the dictionary.

## TypeError

`TypeError` is raised when an operation or function is applied to an object of inappropriate type.

## ValueError

`ValueError` is raised when an operation or function receives an argument of the correct type but with an inappropriate value.

