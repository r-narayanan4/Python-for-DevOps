import subprocess

# Command to check the version of Bash
cmd = ["bash", "--version"]

# Using shell=False as cmd is a list of command arguments
# Using subprocess.PIPE to capture the output and error streams
# Using universal_newlines=True to ensure the output is returned as a string
sp = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

# Wait for the process to complete and capture the return code
rc = sp.wait()

# Capture the output and error streams
o, e = sp.communicate()

# If the return code is 0, the command executed successfully
if rc == 0:
    # Iterate through each line of the output
    for each_line in o.splitlines():
        # Check if the line contains "version" and "release"
        if "version" in each_line and "release" in each_line:
            # Extract and print the version number
            print(each_line.split()[3].split('(')[0])
# If the return code is non-zero, the command failed
else:
    # Print the error message
    print("Command failed and error is:", e)
