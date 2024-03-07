# Loops

## `for` Loop in Python

The `for` loop in Python is used to iterate over a sequence (such as a list, tuple, string, or range) and execute a block of code for each item in the sequence.

## Syntax

```python
for item in sequence:
    # Code block to be executed for each item in the sequence
```

Example:

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


# Output:

apple
banana
cherry
```

Explanation:

- In this example, we have a list of fruits.
- The for loop iterates over each item in the fruits list.
- For each iteration, the loop variable fruit is assigned the current item in the list, and the corresponding code block (printing the fruit) is executed.

## `while` Loop in Python

The `while` loop in Python is used to execute a block of code repeatedly as long as a specified condition is true.

## Syntax

```python
while condition:
    # Code block to be executed while the condition is true
```

Example:

```python

count = 0
while count < 5:
    print(count)
    count += 1
Output:

Copy code
0
1
2
3
4
```

Explanation:

In this example, we initialize a variable count with the value 0.
The while loop continues executing the code block as long as the condition count < 5 is true.
Inside the loop, we print the current value of count and then increment it by 1.

## Nested Loops in Python

Nested loops in Python refer to having one loop inside another loop. They are often used to iterate over elements in multi-dimensional data structures like lists of lists.

## Syntax

```python
for outer_item in outer_sequence:
    for inner_item in inner_sequence:
        # Code block to be executed for each combination of outer_item and inner_item

```

Example:

```python

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for num in row:
        print(num, end=" ")
    print()

# Output:

1 2 3 
4 5 6 
7 8 9 


Explanation:

In this example, we have a list of lists representing a matrix.
The outer loop iterates over each row in the matrix.
The inner loop iterates over each element in the current row.
Inside the inner loop, we print each element of the matrix followed by a space, and use end=" " to prevent a newline after each print statement.
After printing all elements in a row, we print a newline to move to the next row.
```

## Perform different types of iterations

## The `pass` Instruction in Python

In Python, the `pass` statement is a null operation. It is used when a statement is syntactically required but you want to do nothing.

## Usage

The `pass` statement is often used as a placeholder when you are working on unfinished code or when a statement is required syntactically but you don't want any action to be taken.

```python
# Example of using pass
for i in range(5):
    if i == 3:
        pass  # Do nothing when i is equal to 3
    else:
        print(i)

# Output:

0
1
2
4
```

Explanation:

In this example, a for loop iterates over the range of numbers from 0 to 4.
When i is equal to 3, the if statement is executed. Instead of executing any code, the pass statement does nothing, and the loop continues to the next iteration.
For other values of i, the else block is executed, and the value of i is printed.

## Building Loops in Python

In Python, loops are used to execute a block of code repeatedly. There are several ways to build loops using different constructs.

## Using the `while` Loop

The `while` loop in Python is used to execute a block of code repeatedly as long as a specified condition is true.

```python
# Example of using a while loop
count = 0
while count < 5:
    print(count)
    count += 1


# Output:

0
1
2
3
4

Explanation:

In this example, we initialize a variable count with the value 0.
The while loop continues executing the code block as long as the condition count < 5 is true.
Inside the loop, we print the current value of count using the print() function.
After printing the value of count, we increment it by 1 using the count += 1 statement.
The loop repeats until the condition count < 5 is no longer true. Once count becomes equal to 5, the condition becomes false, and the loop terminates.
```

## Using the for Loop

The for loop in Python is used to iterate over a sequence (such as a list, tuple, string, or range) and execute a block of code for each item in the sequence.

## Example of using a for loop with a list

```python

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Output:

apple
banana
cherry

Explanation:

In this example, we have a list of fruits: ["apple", "banana", "cherry"].
The for loop iterates over each item in the fruits list.
For each iteration, the loop variable fruit is assigned the current item in the list.
Inside the loop, we print the value of fruit using the print() function.
The loop continues until all items in the fruits list have been processed.

```



## Using the range() Function

The range() function in Python is used to generate a sequence of numbers. It is commonly used with the for loop to iterate over a sequence of numbers.

```python
# Example of using range() with a for loop
for i in range(5):
    print(i)

# Output:

0
1
2
3
4

Explanation:

In this example, we use the range() function to generate a sequence of numbers from 0 to 4. The range(5) function generates numbers starting from 0 up to (but not including) 5.
The for loop iterates over each number in the sequence generated by range(5).
For each iteration, the loop variable i is assigned the current number from the sequence.
Inside the loop, we print the value of i using the print() function.
The loop continues until all numbers in the sequence generated by range(5) have been processed.

```

## Using the 'in' Keyword

The in keyword in Python is used to check if a value exists in a sequence (such as a list, tuple, string, or dictionary).

```python
# Example of using the in keyword with a list
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Yes, banana is in the list of fruits.")


# Output:

Yes, banana is in the list of fruits.

Explanation:

In this example, we have a list of fruits: ["apple", "banana", "cherry"].
The if statement checks if the string "banana" exists in the fruits list using the in keyword.
Since "banana" is indeed present in the fruits list, the condition evaluates to True, and the corresponding code block (printing "Yes, banana is in the list of fruits.") is executed.
If "banana" were not present in the fruits list, the if condition would evaluate to False, and the code block inside the if statement would not be executed.

```

These are the different ways you can build loops in Python using while, for, range(), and in constructs. Feel free to use them according to your specific requirements.

## Iterating Through Sequences in Python

In Python, you can iterate through sequences (such as lists, tuples, strings, and dictionaries) using loop constructs like `for` loops and `while` loops.

## Using a `for` Loop

The `for` loop is commonly used to iterate through sequences. It iterates over each item in the sequence and executes a block of code for each item.

```python
# Example of iterating through a list with a for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Output:

apple
banana
cherry
```

## Using a while Loop

You can also iterate through sequences using a while loop, although it's less common than using a for loop.

```python

# Example of iterating through a list with a while loop
fruits = ["apple", "banana", "cherry"]
index = 0
while index < len(fruits):
    print(fruits[index])
    index += 1

# Output:

Copy code
apple
banana
cherry

Using either method, you can iterate through sequences to access and process each element individually. The choice between a for loop and a while loop depends on the specific requirements of your code.
```

## Expanding Loops with while-else:

In Python, you can expand loops with the while-else construct. The else block is executed when the loop completes normally (i.e., when the loop condition becomes False), but it is not executed if the loop is terminated by a break statement.

```python

# Example of using a while loop with else
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("Loop completed normally")

# Output:

0
1
2
3
4
Loop completed normally

Explanation:

In this example, a while loop iterates as long as the condition count < 5 is true.
Inside the loop, the current value of count is printed, and then count is incremented by 1.
Once the loop condition becomes False (i.e., when count reaches 5), the else block is executed, printing "Loop completed normally".
```

## Expanding Loops with for-else:

Similarly, you can expand for loops with the for-else construct. The else block in a for loop is executed when the loop completes normally (i.e., when all items in the sequence have been processed), but it is not executed if the loop is terminated by a break statement.

```python

# Example of using a for loop with else
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
else:
    print("All fruits have been processed")

# Output:

apple
banana
cherry
All fruits have been processed

Explanation:

In this example, a for loop iterates over each item in the fruits list.
Inside the loop, each fruit is printed.
Once all items in the fruits list have been processed, the else block is executed, printing "All fruits have been processed".
```

These examples demonstrate how to expand loops with while-else and for-else constructs in Python. They provide a way to execute additional code after the loop completes normally, which can be useful in certain scenarios.

## Nesting Loops and Conditional Statements in Python

Nesting loops and conditional statements in Python involves placing one loop or conditional statement inside another. This allows for more complex control flow and the ability to perform intricate tasks.

## Example

```python
# Example of nesting loops and conditional statements
for i in range(3):
    print("Outer loop iteration:", i)
    for j in range(2):
        print("Inner loop iteration:", j)
        if i == j:
            print("Condition met: i equals j")
        else:
            print("Condition not met: i does not equal j")

# Output:

Outer loop iteration: 0
Inner loop iteration: 0
Condition met: i equals j
Inner loop iteration: 1
Condition not met: i does not equal j
Outer loop iteration: 1
Inner loop iteration: 0
Condition not met: i does not equal j
Inner loop iteration: 1
Condition met: i equals j
Outer loop iteration: 2
Inner loop iteration: 0
Condition not met: i does not equal j
Inner loop iteration: 1
Condition not met: i does not equal j

Explanation:

In this example, we have an outer loop that iterates over the range of numbers from 0 to 2.
Inside the outer loop, we have an inner loop that also iterates over the range of numbers from 0 to 1.
For each iteration of the inner loop, we check a conditional statement (if i == j) to determine if i equals j.
Depending on the outcome of the conditional statement, we print different messages.
This process repeats for each combination of values of i and j, resulting in nested iterations and conditional checks.
Nesting loops and conditional statements allows for the creation of more complex algorithms and the ability to solve a wider range of problems in programming. It's a powerful technique that is commonly used in various applications.

```

## Controlling Loop Execution with `break` and `continue`

In Python, you can control the execution of loops using the `break` and `continue` statements.

## Using `break`

The `break` statement is used to exit the loop prematurely based on a certain condition. When `break` is encountered inside a loop, the loop is terminated immediately, and the program continues executing from the next statement after the loop.

## syntax

```python
for item in iterable:
    if condition:
        break
```

```python
# Example of using break in a loop
for i in range(5):
    if i == 3:
        break
    print(i)

# Output:

0
1
2

Explanation:

In this example, a for loop iterates over the range of numbers from 0 to 4.
Inside the loop, there is an if statement that checks if the current value of i is equal to 3.
When i equals 3, the break statement is executed, causing the loop to terminate immediately.
As a result, only the values 0, 1, and 2 are printed, and the loop exits.

```

## Using continue

The continue statement is used to skip the current iteration of a loop based on a certain condition and continue with the next iteration. When continue is encountered inside a loop, the rest of the code inside the loop for the current iteration is skipped, and the loop moves on to the next iteration.

## syntax

```python
for item in iterable:
    if condition:
        continue

```

```python

# Example of using continue in a loop
for i in range(5):
    if i == 2:
        continue
    print(i)

#Output:

0
1
3
4

Explanation:

In this example, a for loop iterates over the range of numbers from 0 to 4.
Inside the loop, there is an if statement that checks if the current value of i is equal to 2.
When i equals 2, the continue statement is executed, causing the rest of the code inside the loop for that iteration to be skipped.
As a result, the value 2 is not printed, and the loop continues with the next iteration.
Using break and continue statements provides flexibility and control over the execution of loops in Python, allowing you to tailor the behavior of your loops according to specific conditions.

```

## Difference between While and for

| Feature      | `while` Loop                                                                                                             | `for` Loop                                                                                                                                                                                                                                                                               |
|--------------|---------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Usage        | Executes a block of code repeatedly as long as a condition is true.                                                       | Iterates over a sequence or any iterable object.                                                                                                                                                                                                                                        |
| Condition    | Continues iterating until the condition specified becomes false.                                                           | Iterates over each item in the sequence one by one until the sequence is exhausted.                                                                                                                                                                                                      |
| Evaluation   | The condition is evaluated before each iteration. If false initially, the block of code inside the loop may not execute. | The number of iterations is determined by the number of items in the sequence.                                                                                                                                                                                                           |
| Known Before | Typically used when the number of iterations is not known beforehand.                                                      | Typically used when the number of iterations is known beforehand or when you need to iterate over a sequence.                                                                                                                                                                           |

## Example for while Loop:

```python

count = 0
while count < 5:
    print(count)
    count += 1
```

## Example for for Loop:

```python

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

These examples demonstrate how while and for loops are used in Python to achieve different types of iterations.