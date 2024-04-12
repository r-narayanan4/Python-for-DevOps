import csv

# Path to the CSV file to write
req_file = "C:\\Users\\Automation\\Desktop\\hi\\demo.csv"

# Open the CSV file in write mode, specifying 'newline=""' to prevent extra blank lines
fo = open(req_file, 'w', newline="")

# Create a CSV writer object with comma (',') delimiter
csv_writer = csv.writer(fo, delimiter=",")

# Data to write to the CSV file
my_data = [['S_No', "Name", 'Age'], [1, "John", 23], [2, "Cliton", 24]]

# Write the data to the CSV file
csv_writer.writerows(my_data)

# Close the CSV file
fo.close()
