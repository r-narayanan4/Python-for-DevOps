import csv 

# Path to the CSV file
req_file = "C:\\Users\\Automation\\Desktop\\hi\\new_info.csv"

# Open the CSV file in read mode
fo = open(req_file, "r")

# Create a CSV reader object with a pipe delimiter
content = csv.reader(fo, delimiter="|")

# Count the number of rows in the CSV file (excluding the header)
# Note: -1 is subtracted to exclude the header row
print("The no of rows are: ", len(list(content)) - 1)

'''
# Print each row in the CSV file
for each in content:
    print(each)
'''

# Close the CSV file
fo.close()
