# Python Introduction

## What is Python?

Python is a popular programming language created by Guido van Rossum in 1991. It is widely used for various purposes including:

- Web development (server-side)
- Software development
- Mathematics
- System scripting

## What can Python do?

Python's versatility allows it to perform a wide range of tasks such as:

- Creating web applications on servers
- Integrating with software to develop workflows
- Connecting to database systems and manipulating files
- Handling big data and complex mathematical operations
- Rapid prototyping or full-scale software development

## Why Python?

Python offers several advantages:

- Cross-platform compatibility (Windows, Mac, Linux, Raspberry Pi, etc.)
- Simple and readable syntax resembling English
- Concise code requiring fewer lines compared to other languages
- Interpreted execution enabling quick prototyping
- Supports procedural, object-oriented, and functional programming paradigms

## Example

```python
# Get your own Python Server
print("Hello, World!")

```

## What is an Interpreter?

An interpreter is a program that directly executes instructions written in a programming language. In simple terms, it reads and executes code line by line.

## Difference between Interpreter and Compiler

The key difference lies in how they process code:

- **Interpreter**: Executes code line by line, translating each line into machine code or an intermediate form before executing it.
  
- **Compiler**: Translates the entire source code into machine code or an intermediate language before execution, resulting in a standalone executable file.

## Features and Advantages of Python

| Features                                | Advantages                                                                                                 |
|-----------------------------------------|------------------------------------------------------------------------------------------------------------|
| Cross-platform compatibility            | - Can be used on various operating systems like Windows, Mac, Linux, Raspberry Pi, etc.                    |
| Simple and readable syntax             | - Resembles English, making it easy to understand and write code.                                          |
| Concise code                            | - Requires fewer lines compared to other languages, enhancing productivity.                                 |
| Interpreted execution                   | - Enables quick prototyping as code can be executed as soon as it's written.                                |
| Supports multiple programming paradigms | - Provides flexibility to choose from procedural, object-oriented, or functional programming approaches.    |
| Dynamic Typing                          | - Simplifies coding by allowing dynamic typing, reducing the need for explicit type declarations.          |
| Automatic Memory Management             | - Handles memory allocation and deallocation automatically, reducing the risk of memory leaks.             |
| Extensive Standard Library              | - Comes with a rich set of modules and libraries for various tasks, reducing the need for external dependencies. |
| Large Community Support                 | - Open-source nature and wide adoption result in a vast community offering support, libraries, and resources.|
| Ease of Learning and Readability        | - Simple syntax and readability make it easy for beginners to grasp and write code effectively.            |

## Python Indentation

Indentation refers to the spaces at the beginning of a code line.

Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.

Python uses indentation to indicate a block of code.

Example

```python
if 5 > 2:
  print("Five is greater than two!")
```

## Comments

Python has commenting capability for the purpose of in-code documentation.

Comments start with a #, and Python will render the rest of the line as a comment:

Example

```python
# This is a comment.
print("Hello, World!")
```
## Multiline Comments
Python does not really have a syntax for multiline comments.

To add a multiline comment you could insert a # for each line:

```python
# This is a comment
# written in
# more than just one line
print("Hello, World!")
```


Or, not quite as intended, you can use a multiline string.

Since Python will ignore string literals that are not assigned to a variable, you can add a multiline string (triple quotes) in your code, and place your comment inside it:

Example

```python
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")
```

## Understand fundamental terms and definitions

### Interpreting and the Interpreter:

Interpreting is the process of translating and executing code line by line, directly from the source code without prior compilation. An interpreter is a program responsible for this task.

### Compilation and the Compiler:

Compilation is the process of translating the entire source code into machine code or an intermediate language before execution. A compiler is a program responsible for this task.

### Lexis, Syntax, and Semantics:

Lexis refers to the vocabulary or words of a language. Syntax refers to the rules governing the structure of language elements and how they are combined to form valid expressions or statements. Semantics refers to the meaning conveyed by the language elements and the interpretation of those expressions or statements.

### Analogy: Writing a Letter

Imagine you're writing a letter (code) to a friend. The words you choose (lexis) form the vocabulary of your letter. The grammar rules you follow (syntax) dictate how you arrange these words into sentences and paragraphs. Finally, the message you convey (semantics) is the meaning your friend derives from reading your letter.

Example:

```python
# Lexis: Vocabulary of the language
# Syntax: Rules governing the structure
# Semantics: Meaning conveyed by the code

# Example code in Python
x = 5       # Lexis: Assignment statement using variable 'x'
if x == 5:  # Syntax: If statement with comparison
    print("Five!")  # Semantics: Printing the word "Five!"
    
```

## Understand Python’s logic and structure

Keywords:

Python has several keywords that serve as the building blocks for its logic and structure. Some of the important 

keywords include:

| Keyword      | Description                                                                                          | Example Instruction                                                   |
|--------------|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| `if`         | Performs conditional execution based on the truth value of a statement.                              | `if condition:`                                                       |
| `else`       | Used in conjunction with `if` to provide an alternative execution path if the condition is not met. | `else:`                                                              |
| `elif`       | Stands for "else if". Used to check additional conditions if the preceding `if` statement(s) evaluate to False. | `elif condition:`                                            |
| `for`        | Used for looping over an iterable object such as a list, tuple, or string.                            | `for item in iterable:`                                              |
| `while`      | Used to execute a block of code repeatedly as long as a specified condition is true.                  | `while condition:`                                                   |
| `def`        | Used to define a function.                                                                           | `def function_name(parameters):`                                      |
| `return`     | Used inside a function to exit the function and return a value.                                       | `return value`                                                       |
| `and`, `or`, `not` | Used for logical operations (conjunction, disjunction, negation).                                     | `if condition1 and condition2:`                                       |
| `in`         | Used to check if a value exists within a sequence (e.g., a list, tuple, or string).                   | `if element in sequence:`                                            |
| `is`         | Used to test if two variables refer to the same object.                                               | `if variable1 is variable2:`                                          |
| `class`      | Used to define a class.                                                                               | `class ClassName:`                                                    |
| `try`, `except` | Used for exception handling.                                                                         | `try:`                                                               |


Instructions:

Python instructions are the lines of code that you write to carry out specific actions. These instructions can include variable assignments, function calls, conditionals, loops, etc.


Example:

Let's see an example that demonstrates Python's logic and structure:

```python
# Define a function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

# Test the function
num = 11
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

```

In this example:

- We define a function is_prime that takes a number num as input and returns True if it's prime and False otherwise.
- Inside the function, we use conditional statements (if, elif, else) to check if the number is less than or equal to 1, equal to 2, or divisible by any number from 2 up to the square root of the number.
- We test the function by calling it with a number (num = 11) and printing whether it's prime or not based on the returned value from the function.

## Introduce literals and variables into code and use different numeral systems

1.**Literals**: Literals are raw data used in programming. They represent fixed values that are directly used in code. Examples of literals include:

- Boolean literals: True, False
- Integer literals: 42, -10, 0
- Floating-point literals: 3.14, -0.5, 2.0
- String literals: "Hello, world!", 'Python'
- Literal collections: [1, 2, 3], {'key': 'value'}

2.**Variables**: Variables are used to store and manipulate data in a program. They act as containers for storing values that can be referenced and modified throughout the program.

Example:

```python
x = 10
name = "Alice"
```

3.**Boolean**: Boolean values represent truth values and can be either True or False. They are often used in conditional statements and loops to control the flow of a program.

Example:

```python
is_raining = True
has_sunshine = False
```

4.**Integers and Floating-Point Numbers**: Integers are whole numbers, while floating-point numbers have a decimal point. They are used to represent numerical data in Python.

Example:

```python
num_int = 42
num_float = 3.14
```

5.**Scientific Notation**: Scientific notation is a way to represent numbers in a compact form using exponential notation.

Example:

```python
avogadro_number = 6.022e23
```

6.**Strings**: Strings are sequences of characters enclosed in quotes. They are used to represent textual data in Python.

Example:

```python
message = "Hello, world!"
```

6**.Binary, Octal, Decimal, and Hexadecimal Numeral Systems:** These are different numeral systems for representing numbers. In Python, you can represent numbers in binary (0b), octal (0o), decimal, and hexadecimal (0x) formats.

Example:

```python
binary_num = 0b1010
octal_num = 0o17
decimal_num = 15
hexadecimal_num = 0xF
```

7.Naming Conventions: In Python, variables, functions, classes, etc., follow naming conventions outlined in PEP-8. These conventions help maintain consistency and readability in code.

Example:

```python
user_input = "John Doe"
total_sum = 100.5
```

## What is variables?

- Variables are like containers or boxes that hold information in a program.
- They have names (identifiers) that allow us to refer to the data they store.
- The data stored in a variable can change or vary during program execution.

Examples

```python
age = 25
name = "Alice"
is_student = True
```

## What is Data type?

- Data types specify the type of data that can be stored in a variable.
- They define the operations that can be performed on the data.

Examples of data types:

```python
    Integer: age = 25
    String: name = "Alice"
    Boolean: is_student = True
```

In essence, variables are the containers that hold data, and data types specify the type of data that can be stored in those containers. For instance, in the examples provided, age holds an integer value, name holds a string value, and is_student holds a Boolean value.

Below is the list of data types in Python 

| Data Type      | Description                                       | Example                           |
|----------------|---------------------------------------------------|-----------------------------------|
| int            | Represents integers                               | 5, -10, 100                       |
| float          | Represents floating-point numbers                 | 3.14, -0.5, 2.0                   |
| complex        | Represents complex numbers                        | 3 + 4j                            |
| str            | Represents strings                                | "hello", 'world'                  |
| list           | Represents ordered collections of items           | [1, 2, 3], ['a', 'b', 'c']        |
| tuple          | Represents ordered collections of items (immutable) | (1, 2, 3), ('a', 'b', 'c')       |
| dict           | Represents collections of key-value pairs         | {'name': 'Alice', 'age': 30}      |
| set            | Represents unordered collections of unique items   | {1, 2, 3}                         |
| frozenset      | Represents immutable sets                         | frozenset({1, 2, 3})              |
| bool           | Represents Boolean values                         | True, False                       |
| NoneType       | Represents the absence of a value or a null value | None                              |

