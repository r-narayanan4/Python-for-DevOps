# Conditional Statements and Branching in Python

In programming, conditional statements allow us to make decisions and control the flow of execution based on certain conditions. Python provides several conditional statements: `if`, `if-else`, `if-elif`, and `if-elif-else`.

## `if` Statement

The `if` statement checks whether a condition is true or false. If the condition is true, the code block inside the `if` statement is executed.

### Syntax

```python
if condition:
    # Code block to be executed if condition is true
```

Example

```python
x = 10
if x > 5:
    print("x is greater than 5")

Output Explanation:

x is greater than 5

Explanation: Since the condition x > 5 evaluates to True (since x is 10 which is greater than 5), the statement inside the if block is executed, printing "x is greater than 5".

```

## `if-else` Statement

The `if-else` statement in Python allows us to execute one block of code if a condition is true and another block if the condition is false.

### Syntax

```python
if condition:
    # Code block to be executed if condition is true
else:
    # Code block to be executed if condition is false

```

Example:

```python

x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

```

Output Explanation:

x is greater than 5

Explanation: Since the condition x > 5 evaluates to True (since x is 10 which is greater than 5), the statement inside the if block is executed, printing "x is greater than 5". If the condition was false, the statement inside the else block would have been executed instead.

## `if-elif` Statement

The `if-elif` statement in Python allows us to check multiple conditions and execute a block of code corresponding to the first true condition encountered.

### Syntax

```python
if condition1:
    # Code block to be executed if condition1 is true
elif condition2:
    # Code block to be executed if condition2 is true
# Add more elif statements if needed
else:
    # Code block to be executed if none of the above conditions are true
```

Example:

```python
x = 10
if x > 10:
    print("x is greater than 10")
elif x < 10:
    print("x is less than 10")
else:
    print("x is equal to 10")

# Output Explanation:

x is equal to 10

# Explanation: 

In this example, the condition x > 10 is not true, so it moves to the next elif statement. The condition x < 10 is also not true. Finally, the else block is executed since none of the previous conditions are true, printing "x is equal to 10".

```

## `if-elif-elif-else` Statement

The `if-elif-elif-else` statement in Python allows us to check multiple conditions and execute a block of code corresponding to the first true condition encountered. If none of the conditions are true, the `else` block is executed.

### Syntax

```python
if condition1:
    # Code block to be executed if condition1 is true
elif condition2:
    # Code block to be executed if condition2 is true
elif condition3:
    # Code block to be executed if condition3 is true
# Add more elif statements if needed
else:
    # Code block to be executed if none of the above conditions are true
```

Example:

```python

x = 10
if x > 10:
    print("x is greater than 10")
elif x < 10:
    print("x is less than 10")
elif x == 10:
    print("x is equal to 10")
else:
    print("x is not a number")

Output Explanation:

x is equal to 10

Explanation: In this example, the condition x > 10 is not true, so it moves to the next elif statement. The condition x < 10 is also not true. Then, the condition x == 10 is true, so the corresponding code block is executed, printing "x is equal to 10". Since one of the conditions is true, the else block is skipped.

```

## Multiple Conditional Statements

In Python, you can have multiple `if` statements to check different conditions independently.

### Syntax

```python
if condition1:
    # Code block to be executed if condition1 is true

if condition2:
    # Code block to be executed if condition2 is true

# Add more if statements as needed
```

Example:

```python

x = 10
if x > 5:
    print("x is greater than 5")

if x < 15:
    print("x is less than 15")


Output Explanation:

x is greater than 5
x is less than 15

Explanation: Both conditions are evaluated independently. If x is greater than 5, the first print statement will execute. Similarly, if x is less than 15, the second print statement will execute.
```

## Nesting Conditional Statements

In Python, you can nest conditional statements within each other to create more complex conditions.

### Syntax

```python

if condition1:
    if condition2:
        # Code block to be executed if both condition1 and condition2 are true
    else:
        # Code block to be executed if condition1 is true and condition2 is false
else:
    # Code block to be executed if condition1 is false
```

Example:

```python

x = 10
if x > 5:
    if x < 15:
        print("x is between 5 and 15")
    else:
        print("x is greater than or equal to 15")
else:
    print("x is less than or equal to 5")

Output Explanation:

x is between 5 and 15

Explanation: In this example, the outer if statement checks if x is greater than 5. If true, it enters the inner if, which checks if x is less than 15. Depending on the values, different print statements will be executed. If the outer if condition is false, it executes the else block.

```
