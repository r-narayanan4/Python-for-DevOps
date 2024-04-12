#sfile="C:\\Users\\Automation\\Desktop\\random.txt"
#dfile="C:\\Users\\Automation\\Downloads\\newrandom.txt"
# Prompting the user to input the source file path
sfile=input("Enter your source file: ")

# Prompting the user to input the destination file path
dfile=input("Enter your destination file: ")

# Opening the source file in read mode
sfo=open(sfile,'r')

# Reading the content of the source file
content=sfo.read()

# Closing the source file
sfo.close()

# Opening the destination file in write mode
dfo=open(dfile,'w')

# Writing the content read from the source file to the destination file
dfo.write(content)

# Closing the destination file
dfo.close()
