# datetime module

# The datetime module is a built-in or default module in Python, used for working with dates and times.

# To create log files with date and time stamps, we can use the datetime module.

# Importing the datetime module
import datetime

# Printing the current date and time using datetime.now()
print(datetime.datetime.now())

# Printing the current date and time using datetime.today()
print(datetime.datetime.today())

# Both datetime.now() and datetime.today() give the same result for the time zone set by default in the system.

# If you want to get time in a specific time zone, such as IST (Indian Standard Time),
# you need to use datetime.now() with a timezone object created using pytz module.

# What is pytz module?
# pytz is a third-party module in Python used for working with time zones. It provides functionality to create timezone objects and perform timezone conversions.

# Importing the pytz module
import pytz

# Creating a timezone object for IST (Indian Standard Time)
ist = pytz.timezone('Asia/Kolkata')

# Printing the current date and time in the IST timezone
print(datetime.datetime.now(ist))

# Note: When working with specific timezones, use datetime.now() with the timezone object, not datetime.today().

# Additional operations with datetime module:

# Getting individual components of the current date and time
print(datetime.datetime.now().year)
print(datetime.datetime.now().month)
print(datetime.datetime.now().day)
print(datetime.datetime.now().hour)
print(datetime.datetime.now().minute)
print(datetime.datetime.now().second)

# Formatting the current date and time
print(datetime.datetime.now().strftime("%y-%m-%d"))
print(datetime.datetime.now().strftime("%Y-%m-%d"))
print(datetime.datetime.now().strftime("%c"))

# More formatting options can be found on strftime.org

# Accessing contents of the datetime.datetime class using dir()
print(dir(datetime.datetime))

# Creating a datetime object from a timestamp
print(datetime.datetime.fromtimestamp(155555))

# Printing the maximum representable datetime
print(datetime.datetime.max)

# Importing datetime class directly for convenience
from datetime import datetime

# Printing the current date and time using datetime.now() after direct import
print(datetime.now())

