#NameError
#TypeError
#FileNotFoundError
#ZeroDivisionError

try:
    print("This is try block")
    import fabric  # This line tries to import a module that doesn't exist, which will raise an ImportError
    print(a)  # This line tries to access an undefined variable, which will raise a NameError
    #print(4+"hi")  # This line tries to add an integer and a string, which will raise a TypeError
    #open('asdfas.txt')  # This line tries to open a file that doesn't exist, which will raise a FileNotFoundError
    #print(5/0)  # This line tries to divide by zero, which will raise a ZeroDivisionError
except FileNotFoundError:
    print("File is not present to open it")
except NameError:
    print("Variable is not defined")
except TypeError:
    print("Adding number and string is not possible")
except ZeroDivisionError:
    print("Division with zero is not possible")
except ModuleNotFoundError:
    print("Please install fabric to use it")
except Exception as e:
    print(e)  # This except block handles any other exceptions not explicitly mentioned above
finally:
    print("Finally this will execute")  # This block always executes, regardless of whether an exception occurs or not
