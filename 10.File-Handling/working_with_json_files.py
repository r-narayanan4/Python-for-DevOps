import json 

# Reading from a JSON file
req_file = "myjson.json"  # File to read from

fo = open(req_file, 'r')  # Open the file in read mode
# Load the JSON data from the file and print it
print(json.load(fo))
fo.close()  # Close the file

# Writing data (dictionary data) into a JSON file
my_dict = {'Name': 'rln', 'skills': ['Python', 'shell', 'yaml', 'AWS']}  # Data to write

req_file = "myinfo.json"  # File to write to

fo = open(req_file, 'w')  # Open the file in write mode
# Write the dictionary data into the file in JSON format with indentation
json.dump(my_dict, fo, indent=4)
fo.close()  # Close the file
