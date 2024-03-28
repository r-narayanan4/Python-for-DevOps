# Example 1: Creating a dictionary from a list
numbers = [1, 2, 3, 4, 5]
squared_numbers = {x: x*x for x in numbers}
print(squared_numbers)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Example 2: Creating a dictionary with conditional logic
even_numbers = {x: x*x for x in numbers if x % 2 == 0}
print(even_numbers)  # Output: {2: 4, 4: 16}

# Example 3: Creating a dictionary from two lists
keys = ['a', 'b', 'c']
values = [1, 2, 3]
combined_dict = {k: v for k, v in zip(keys, values)}
print(combined_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}

'''Dictionary comprehension is a concise way to create dictionaries in Python using a single line of code. It allows you to generate dictionaries dynamically from any iterable, such as lists, tuples, or even other dictionaries.

Here's the general syntax for dictionary comprehension:
{key_expression: value_expression for item in iterable}

key_expression: Expression that generates keys for the dictionary.
value_expression: Expression that generates values for the dictionary.
item: Represents each item in the iterable.
iterable: The iterable object from which to create the dictionary.


'''