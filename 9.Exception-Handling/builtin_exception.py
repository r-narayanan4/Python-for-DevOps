# Combined Examples

import sys

# Example for BaseException
try:
    # Connect to a database
    # ...
    raise BaseException("Failed to connect to the database")
except BaseException as e:
    print("Error occurred:", e)

# Example for Exception
class DeploymentException(Exception):
    pass

try:
    # Deploy application
    # ...
    raise DeploymentException("Failed to deploy application")
except Exception as e:
    print("Deployment error:", e)

# Example for SystemExit
try:
    # Check if resources are available
    # ...
    sys.exit(0)
except SystemExit:
    print("Exiting the resource checking process")

# Example for KeyboardInterrupt
try:
    # Continuous monitoring of server logs
    while True:
        # Analyze logs
        # ...
        pass
except KeyboardInterrupt:
    print("Server log monitoring interrupted by user")

# Example for ArithmeticError
try:
    result = 10 / 0
except ArithmeticError as e:
    print("Caught an arithmetic error:", e)

# Example for LookupError
try:
    d = {'a': 1, 'b': 2}
    print(d['c'])
except LookupError as e:
    print("Caught a lookup error:", e)

# Example for IndexError
try:
    l = [1, 2, 3]
    print(l[4])
except IndexError as e:
    print("Caught an index error:", e)

# Example for KeyError
try:
    d = {'a': 1, 'b': 2}
    print(d['c'])
except KeyError as e:
    print("Caught a key error:", e)

# Example for TypeError
try:
    result = 10 + "hello"
except TypeError as e:
    print("Caught a type error:", e)

# Example for ValueError
try:
    int("abc")
except ValueError as e:
    print("Caught a value error:", e)

    
