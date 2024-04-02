'''
Name hiding, also known as shadowing, occurs when a variable in a local scope (like within a function) has the same name as a variable in an outer scope (like in the global scope). This local variable "shadows" or hides the outer variable within its scope, making it inaccessible within that scope.

Name hiding, also known as shadowing, occurs when a variable defined within a certain scope has the same name as another variable in an outer scope. In such cases, the inner variable "shadows" or hides the outer variable, making the outer variable inaccessible within the inner scope. This concept can lead to confusion and unintended behavior in your code, so it's essential to understand how name hiding works.

'''
# This is a Python example demonstrating name hiding (shadowing).

outer_var = 10

def my_function():
    outer_var = 20  # This shadows the outer_var defined outside the function.
    print("Inside the function, outer_var:", outer_var)

def another_function():
    print("Inside another_function, outer_var:", outer_var)

# Global scope:
print("Outside all scopes, outer_var:", outer_var)

# Function scope:
my_function()  # This function will print the value of the inner (shadowed) outer_var.
another_function()  # This function will print the value of the outer_var from the global scope.


# Output:

# Outside all scopes, outer_var: 10
# Inside the function, outer_var: 20
# Inside another_function, outer_var: 10

# In this example:

# There are two variables named outer_var: one in the global scope and another within the my_function() function.
# When my_function() is called, it prints the value of the outer_var defined within its scope, which is 20 (the inner one, shadowing the outer one).
# When another_function() is called, it prints the value of the outer_var from the global scope, which is 10.
# This demonstrates how the inner variable can hide the outer variable within its scope, leading to potential confusion if not managed carefully.





