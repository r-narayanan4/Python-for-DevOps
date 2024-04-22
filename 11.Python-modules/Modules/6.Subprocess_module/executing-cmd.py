# Subprocess Module 

#The subprocess module is used to execute operating system commands and store the output into a variable.

""""
import subprocess
sp=subprocess.Popen(cmd,shell=True/False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
out,err=sp.communicate()
print(f'OUTPUT IS: {out}')
print(f'Error is: {err}')
==================================>
if shell=True then your cmd is a string (as your os command)
if shell=False then your cmd is a list

Note: shell=False dont work on your os environment variables
      
ex: cmd="ls -lrt" ==>shell=True
    shell=False ==> cmd="ls -lrt".split()  or ['ls','-lrt']
=======================================================================


shell=True always on windows
============================
cmd is a string
----------------------------------------------------------
"""


import subprocess

# Importing the subprocess module for executing operating system commands
# Command to list files in long format
cmd = "ls -lrt"

# Using shell=True/False to specify if the command should be interpreted through a shell or not
# If shell=True, cmd is a string; if shell=False, cmd should be a list of command arguments
# Using subprocess.PIPE to capture the output and error streams
# Using universal_newlines=True to ensure the output is returned as a string
sp = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

# Wait for the process to complete and capture the return code
rc = sp.wait()

# Capture the output and error streams
out, err = sp.communicate()

# Print the return code
print(f'The return code: {rc}')

# Print the output and error streams
print(f'OUTPUT IS: \n{out}')
print(f'Error is: \n{err}')

# Print the output and error streams as lists of lines
print(f'OUTPUT IS: \n{out.splitlines()}')
print(f'Error is: \n{err.splitlines()}')
