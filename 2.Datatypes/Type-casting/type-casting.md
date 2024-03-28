# Type Casting in Python

Type casting, also known as type conversion, refers to the process of changing the data type of a variable from one type to another. This is often necessary when working with different types of data or when performing operations that require data of a specific type.

In Python, type casting can be done using built-in functions or constructors that are available for each data type. Some common type casting functions include:

- `int()` to convert a value to an integer.
- `float()` to convert a value to a floating-point number.
- `str()` to convert a value to a string.
- `bool()` to convert a value to a boolean (True or False).

For example:

```python
# Convert a string to an integer
string_number = "123"
integer_number = int(string_number)
print(integer_number)  # Output: 123

# Convert a floating-point number to an integer
float_number = 3.14
integer_number = int(float_number)
print(integer_number)  # Output: 3

# Convert an integer to a string
integer_number = 123
string_number = str(integer_number)
print(string_number)  # Output: "123"

# Convert a boolean to an integer
boolean_value = True
integer_value = int(boolean_value)
print(integer_value)  # Output: 1 (True is represented as 1)

# Convert an integer to a boolean
integer_value = 0
boolean_value = bool(integer_value)
print(boolean_value)  # Output: False (0 is represented as False)
```

example

```python

# Convert a string to a floating-point number
string_number = "3.14"
float_number = float(string_number)
print(float_number)  # Output: 3.14

# Convert a floating-point number to a string
float_number = 3.14
string_number = str(float_number)
print(string_number)  # Output: "3.14"

# Convert a boolean to a string
boolean_value = True
string_value = str(boolean_value)
print(string_value)  # Output: "True"

# Convert a string to a boolean
string_value = "False"
boolean_value = bool(string_value)
print(boolean_value)  # Output: True (Non-empty strings are considered True)

# Convert an integer to a floating-point number
integer_number = 5
float_number = float(integer_number)
print(float_number)  # Output: 5.0

# Convert a floating-point number to an integer
float_number = 3.99
integer_number = int(float_number)
print(integer_number)  # Output: 3 (truncates the decimal part)
```
