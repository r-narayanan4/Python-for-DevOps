'''
The global keyword in Python is used to indicate that a variable declared within a function should be treated as a global variable. This means that it can be accessed and modified from both within the function and from outside the function, in the global scope.

Here's a simple explanation with an example:

'''
# Global variable
global_var = 10

def my_function():
    # Using global keyword to modify global variable within the function
    global global_var
    global_var = 20
    print("Inside the function, global_var:", global_var)

# Global scope
print("Before calling the function, global_var:", global_var)

# Function call
my_function()

# Global scope after function call
print("After calling the function, global_var:", global_var)

# Output:

# Before calling the function, global_var: 10
# Inside the function, global_var: 20
# After calling the function, global_var: 20


# In this example:

# There's a global variable global_var with an initial value of 10.
# Inside the my_function() function, the global keyword is used to declare global_var as a global variable.
# Within the function, the value of global_var is modified to 20.
# After calling the function, the value of global_var in the global scope is indeed changed to 20, demonstrating that the function was able to modify the global variable due to the use of the global keyword.