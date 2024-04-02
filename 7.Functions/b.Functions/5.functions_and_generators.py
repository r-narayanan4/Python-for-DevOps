"""
User-Defined Functions:

User-defined functions are blocks of reusable code that perform a specific task. They allow you to encapsulate logic into a single named entity, making your code more organized, modular, and easier to understand. User-defined functions are defined using the 'def' keyword followed by the function name and a block of code that specifies what the function does. They can take zero or more arguments as input and optionally return a value using the 'return' statement. User-defined functions are commonly used to break down complex tasks into smaller, manageable parts, improve code readability, and promote code reuse across multiple parts of a program.

Generators:

Generators in Python are special types of iterators that allow you to generate a sequence of values lazily on-the-fly. Unlike traditional functions that compute and return all values at once, generators produce values dynamically as they are requested, pausing and resuming execution using the 'yield' statement. This lazy evaluation approach makes generators memory-efficient and suitable for processing large datasets or infinite sequences. Generator functions are defined using the 'def' keyword with 'yield' statements to yield values instead of 'return'. Generator objects are created by calling the generator function and can be iterated over using 'for' loops or functions like 'next()' to generate values one at a time. Generators are commonly used in situations where you need to generate sequences of values efficiently, especially when dealing with large datasets or infinite sequences.
"""
"""
Differences between User-Defined Functions and Generators:

1. Execution:
   - User-defined functions execute all statements within the function body when called.
   - Generators execute lazily, meaning they produce values on-the-fly and pause execution between each yield statement.

2. Return Values:
   - User-defined functions use the return statement to return a value or None if no return statement is present.
   - Generators use the yield statement to produce a sequence of values, allowing them to generate values dynamically.

3. State Retention:
   - User-defined functions do not retain their state between calls, as each function call starts execution from the beginning.
   - Generators retain their state between calls, allowing them to remember where they left off and continue execution from the last state.

4. Memory Usage:
   - User-defined functions may consume more memory, especially if they generate large datasets or perform heavy computations.
   - Generators are memory-efficient, as they generate values on-the-fly and consume memory only for the current state, making them suitable for processing large datasets or infinite sequences.

5. Iteration:
   - User-defined functions may use iterators or loops to generate sequences of values, but they typically compute all values upfront.
   - Generators are inherently iterable, allowing them to produce values dynamically in a loop or using iterator functions like next().

6. Use Cases:
   - User-defined functions are suitable for encapsulating reusable logic that performs specific tasks or computations.
   - Generators are useful for generating sequences of values lazily, processing large datasets, implementing data streaming, and creating infinite sequences efficiently.

7. Syntax:
   - User-defined functions are defined using the def keyword and may contain multiple return statements to return values.
   - Generators are defined using the def keyword with yield statements to produce values, indicating that the function is a generator.

Overall, while both user-defined functions and generators enable encapsulating logic into reusable components, they differ in execution behavior, return values, state retention, memory usage, and use cases, making each suitable for specific programming scenarios.
"""
"""
User-Defined Functions and Generators

This Python file provides examples and explanations of user-defined functions and generators.
"""

def user_defined_function(x):
    """
    A user-defined function to calculate the square of a number.
    """
    return x * x

def generator_function(n):
    """
    A generator function to generate squares of numbers from 1 to n.
    """
    for i in range(1, n + 1):
        yield i * i

def main():
    """
    Main function to demonstrate the usage of user-defined functions and generators.
    """
    # Define a number
    num = 5

    # Demonstrate invoking the user-defined function
    print("Square of", num, "using user-defined function:", user_defined_function(num))

    # Demonstrate invoking the user-defined generator
    print("Squares of numbers up to", num, "using user-defined generator:")
    for result in generator_function(num):
        print(result, end=" ")

# Invoke the main function
if __name__ == "__main__":
    main()

# Output:

# Square of 5 using user-defined function: 25
# Squares of numbers up to 5 using user-defined generator:
# 1 4 9 16 25

# Explanation:

# User-Defined Functions:

# The user_defined_function calculates the square of a number. In the main function, it's called with num as an argument (user_defined_function(num)), where num is 5. So, it returns 5*5, which is 25.
# Generators:

# The generator_function generates squares of numbers from 1 to n. In the main function, it's called with num as an argument (generator_function(num)), where num is 5. It then yields squares of numbers from 1 to 5 (1, 4, 9, 16, 25) when iterated over using a for loop.
# The output demonstrates the usage of both user-defined functions and generators, showcasing how they encapsulate logic into reusable components and produce the desired results.

