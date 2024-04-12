'''
age = 23

# Check if age is greater than 30
if age > 30:
    print("Valid age")
else:
    # Raise a ValueError if age is less than or equal to 30
    raise ValueError("Age is less than 30")
'''

age = 20

try:
    # Check if age is greater than 30 using assert statement
    assert age > 30
    print("Valid age")
except AssertionError:
    # Handle AssertionError raised by assert statement
    print("Raised with assert because age is less than 30")
except:
    # Handle any other exceptions
    print("Exception occurred")
