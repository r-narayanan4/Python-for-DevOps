# Python Operators

Operators are used to perform operations on variables and values.

- Arithmetic Operators
- Assignment Operators
- Comparison Operators or Relational Operators
- Logical Operators
- Identity Operators
- Membership Operators
- Bitwise Operators


## Python divides its operators into several groups:

## Arithmetic Operators

Arithmetic operators are used for performing mathematical operations like addition, subtraction, multiplication, etc.

- `+` Addition
- `-` Subtraction
- `*` Multiplication
- `/` Division
- `%` Modulus (remainder of the division)
- `**` Exponentiation (power)
- `//` Floor division (quotient of the division)

## Assignment Operators

Assignment operators are used to assign values to variables.

- `=` Assign value
- `+=` Add and assign
- `-=` Subtract and assign
- `*=` Multiply and assign
- `/=` Divide and assign
- `%=` Modulus and assign
- `**=` Exponentiation and assign
- `//=` Floor division and assign

## Comparison Operators

Comparison operators are used to compare values.

- `==` Equal to
- `!=` Not equal to
- `>` Greater than
- `<` Less than
- `>=` Greater than or equal to
- `<=` Less than or equal to

## Logical Operators

Logical operators are used to combine conditional statements.

- `and` Logical AND
- `or` Logical OR
- `not` Logical NOT

## Identity Operators

Identity operators are used to compare the memory locations of two objects.

- `is` Returns true if both variables are the same object
- `is not` Returns true if both variables are not the same object

## Membership Operators

Membership operators are used to test if a sequence is presented in an object.

- `in` Returns true if a sequence with the specified value is present in the object
- `not in` Returns true if a sequence with the specified value is not present in the object

## Bitwise Operators

Bitwise operators are used to perform bitwise operations on integers.

- `&` Bitwise AND
- `|` Bitwise OR
- `^` Bitwise XOR
- `~` Bitwise NOT
- `<<` Left shift
- `>>` Right shift

Explanation:

- `&` (Bitwise AND): Performs the AND operation on each pair of corresponding bits. The result is 1 only if both bits are 1, otherwise, it's 0.

- `|` (Bitwise OR): Performs the OR operation on each pair of corresponding bits. The result is 1 if at least one of the bits is 1, otherwise, it's 0.

- `^` (Bitwise XOR): Performs the exclusive OR (XOR) operation on each pair of corresponding bits. The result is 1 if the bits are different, otherwise, it's 0.

- `~` (Bitwise NOT): Performs the NOT operation on each bit, which means it flips each bit from 0 to 1 and from 1 to 0.

- `<<` (Left shift): Shifts the bits of a number to the left by a certain number of positions, filling the empty positions with zeros.

- `>>` (Right shift): Shifts the bits of a number to the right by a certain number of positions, filling the empty positions with zeros or the sign bit (for signed integers).


# Left Shift and Right Shift in Python

In Python, left shift (`<<`) and right shift (`>>`) are bitwise shift operators used to manipulate binary numbers.

## Left Shift (`<<`)

- Left shifting a binary number involves moving each digit in the binary representation of the number to the left by a certain number of positions.
- For each position shifted left, the number effectively gets multiplied by 2.
- Example: If we have the binary number `101` (which represents `5` in decimal) and we left shift it by `2` positions (`101 << 2`), we get `10100`, which represents `20` in decimal.

Left Shift (<<):

Left shifting 101 (which represents 5 in decimal) by 2 positions (101 << 2):

```sql
Start:       101   (5 in binary)
Left shift:  10100 (Shifted left by 2 positions)
```
In this case, 101 (binary for 5) is shifted to the left by 2 positions. Two 0s are added to the right.

## Right Shift (`>>`)

- Right shifting a binary number involves moving each digit in the binary representation of the number to the right by a certain number of positions.
- For each position shifted right, the number effectively gets divided by 2 (discarding any remainders).
- Example: If we have the binary number `101` (which represents `5` in decimal) and we right shift it by `1` position (`101 >> 1`), we get `10`, which represents `2` in decimal.

Right Shift (>>):

Right shifting 101 (which represents 5 in decimal) by 1 position (101 >> 1):

```sql
Start:       101   (5 in binary)
Right shift:  10   (Shifted right by 1 position)
```

eval function:

 `eval()` function in Python evaluates a string containing a Python expression and returns the result of that expression. It's a powerful but potentially risky function, as it can execute arbitrary code.

 ```python
print(eval("3 * (4 + 5) / 2"))
 ```

Command Line Arguments:

Command-line arguments in Python are the arguments passed to a Python script when it is executed from the command line. These arguments allow you to customize the behavior of the script without modifying its code. You can pass information to the script such as file paths, options, parameters, or any other data.

Python provides a built-in module called sys that allows you to access command-line arguments via the `sys.argv` list. The `sys.argv` list contains all the command-line arguments passed to the script, where `sys.argv[0]` is the script name itself and subsequent elements contain the arguments.

