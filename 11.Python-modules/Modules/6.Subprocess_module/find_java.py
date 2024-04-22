import subprocess

# Command to check the Java version
cmd = "java -version"

# Execute the command using subprocess.Popen
sp = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

# Wait for the process to complete and capture the return code
rc = sp.wait()

# Capture the output and error streams
o, e = sp.communicate()

# Check if the command executed successfully (return code 0)
if rc == 0:
    # If there's output (stdout), print it
    if o:
        print(o)
    # If there's no output but there's an error message (stderr), print the version extracted from the error message
    elif e:
        # Extract and print the version from the error message
        print(e.splitlines()[0].split()[2].strip("\""))
# If the return code is non-zero, print the error message
else:
    print(e)
