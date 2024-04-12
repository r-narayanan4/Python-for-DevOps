try:
    a = 9
    print(a)  # This line prints the value of 'a'
except NameError:
    print("Variable is not defined")
except Exception as e:
    print("Exception occurred:", e)  # This block handles any other exceptions not explicitly mentioned above
else:
    print("This will execute if there are no exceptions in the try block")  # This block executes if no exceptions occur in the try block
finally:
    print("This will execute always")  # This block always executes, regardless of whether an exception occurs or not
