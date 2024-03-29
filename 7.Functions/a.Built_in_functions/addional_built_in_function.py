import os
import subprocess
from datetime import datetime
import time
import logging

# Get the current directory path
current_directory = os.path.dirname(os.path.abspath(__file__))
# Configure logging
log_file_path = os.path.join(current_directory, 'example.log')
logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(message)s')

# Check if a file exists or create it
file_path = os.path.join(current_directory, 'example_file.txt')
if not os.path.exists(file_path):
    with open(file_path, 'w') as f:
        f.write("This file was created by the script.\n")
    logging.info(f"Created file '{file_path}'.")

# Check if a path is a file
if os.path.isfile(file_path):
    if os.path.getsize(file_path) == 0:
        with open(file_path, 'w') as f:
            f.write("This file was created by the script.\n")
        logging.info(f"'{file_path}' is an empty file and was created by the script.")
    else:
        logging.info(f"'{file_path}' is a file.")
else:
    logging.info(f"'{file_path}' is not a file.")

# Check if a path is a directory
dir_path = os.path.join(current_directory, 'example_directory')
if not os.path.exists(dir_path):
    os.makedirs(dir_path)
    logging.info(f"Created directory '{dir_path}'.")
elif len(os.listdir(dir_path)) == 0:
    # If the directory is empty, create an empty file with a note
    empty_file_path = os.path.join(dir_path, 'empty_file.txt')
    with open(empty_file_path, 'w') as f:
        f.write("This directory was created by the script.\n")
    logging.info(f"Created empty file '{empty_file_path}' in directory '{dir_path}'.")

# List files and directories in a path
logging.info(f"Contents of '{dir_path}': {os.listdir(dir_path)}")

# Run a command with arguments
subprocess.run(['ls', '-l'])

# Get current date and time
current_datetime = datetime.now()
logging.info(f"Current date and time: {current_datetime}")

# Suspend execution for 2 seconds
logging.info("Waiting for 2 seconds...")
time.sleep(2)
logging.info("Wait complete.")
