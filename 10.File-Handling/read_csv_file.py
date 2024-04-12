import csv 

# Path to the CSV file
req_file = "C:\\Users\\Automation\\Desktop\\hi\\new_info.csv"

# Open the CSV file in read mode
fo = open(req_file, "r")

# Create a CSV reader object with a pipe delimiter
content = csv.reader(fo, delimiter="|")

# Iterate over each row in the CSV file
for row in content:
    # Print each row
    print(row)

# Close the CSV file
fo.close()
