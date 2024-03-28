# Data Structures in Python

Python provides several built-in data structures to store collections of data. Here are some commonly used data structures:

## Lists

A list is a mutable, ordered collection of elements. Each element in a list is indexed by its position, starting from 0.

Example:

```python
# Creating a list
my_list = [1, 2, 3, 4, 5]

# Accessing elements of a list
print(my_list[0])  # Output: 1

# Modifying elements of a list
my_list[2] = 10
print(my_list)  # Output: [1, 2, 10, 4, 5]

Explanation:

Lists are versatile and commonly used data structures in Python.
They can contain elements of different data types and can be easily modified.
Lists are indexed, meaning you can access elements by their position using square brackets [ ].
Lists are mutable, allowing you to modify, add, or remove elements after creation.
You can modify elements of a list using indexing and assignment.
```

## Tuples

A tuple is an immutable, ordered collection of elements. Once created, the elements of a tuple cannot be modified.

Example:

```python
# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# Accessing elements of a tuple
print(my_tuple[0])  # Output: 1

Explanation:

Tuples are similar to lists, but they are immutable, meaning their elements cannot be changed after creation.
They are often used to store collections of items that should not be modified, such as coordinates, database records, or function return values.
You can access elements of a tuple using indexing, similar to lists.
Once created, the elements of a tuple cannot be modified or reassigned.
```

## Sets

A set is a mutable, unordered collection of unique elements. Sets are useful for performing mathematical set operations like union, intersection, etc.

Example:

```python
# Creating a set
my_set = {1, 2, 3, 4, 5}

# Adding elements to a set
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

Explanation:

Sets are collections of unique elements, meaning each element appears only once in the set.
Sets are unordered, so the elements are not indexed and cannot be accessed by their position.
You can add elements to a set using the add() method.
Sets are mutable, allowing you to modify, add, or remove elements after creation.
Sets are commonly used for tasks involving unique elements or mathematical operations like union, intersection, difference, etc.
```

## Strings

A string is an immutable sequence of characters. Strings can be created using single quotes (''), double quotes ("") or triple quotes (''' or """).

Example:

```python
# Creating strings
my_string1 = 'Hello'
my_string2 = "World"
my_string3 = '''Python'''

# Concatenating strings
concatenated_string = my_string1 + ' ' + my_string2
print(concatenated_string)  # Output: Hello World

Explanation:

Strings are sequences of characters, enclosed within single quotes (''), double quotes ("") or triple quotes (''' or """).
Strings are immutable, meaning their contents cannot be changed after creation.
You can concatenate strings using the + operator.
Strings support various operations and methods for manipulation, searching, and formatting.
```

## Dictionaries

A dictionary is an unordered collection of key-value pairs. Each key-value pair maps the key to its corresponding value.

Example:

```python
# Creating a dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Accessing values in a dictionary
print(my_dict['name'])  # Output: John

# Modifying values in a dictionary
my_dict['age'] = 35
print(my_dict)  # Output: {'name': 'John', 'age': 35, 'city': 'New York'}

Explanation:

Dictionaries are data structures that store key-value pairs, where each key maps to a corresponding value.
Keys within a dictionary must be unique, and they are typically immutable types like strings or numbers.
Values within a dictionary can be of any data type and can be mutable or immutable.
Dictionaries are unordered, meaning the order of key-value pairs may not be preserved.
You can access values in a dictionary using square brackets [] and providing the key.
You can modify values in a dictionary by assigning a new value to a key.
```
