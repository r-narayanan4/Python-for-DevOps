# This section creates a new text file named 'newdemo.txt' with write mode,
# but the file isn't utilized further in the provided code.
'''
fo=open('newdemo.txt','w')
#print(fo.mode)
#print(fo.readable())
#print(fo.writable())
fo.close()
'''

# This section writes three lines of text to a file named 'random.txt'
# and then closes the file.
'''
my_content=["This is a data -1\n","This is a data-2\n","This is a data-3"]
fo=open("random.txt",'w')
fo.write("This is a first line\n")
fo.write("This is a second line\n")
fo.write("This is a third line")
#fo.writelines(my_content)
fo.close()
'''

# This section appends three lines of text to a file named 'with_loop.txt' using a loop,
# and then closes the file.
'''
my_content=['This is using loop-iteratioin-1','This is using loop-iterantion-2','This is using loop-iteratioin-3']

fo=open("with_loop.txt",'a')

for each_line in my_content:
	fo.write(each_line+"\n")
fo.close()
'''

# This section reads the entire contents of the file 'with_loop.txt' and prints it.
'''
fo=open("with_loop.txt","r")
data=fo.read()
fo.close()

print(data)
'''

# This section reads the first two lines of the file 'with_loop.txt' and prints them.
'''
fo=open("with_loop.txt","r")
print(fo.readline())
print(fo.readline())
fo.close()
'''

# This section reads all the lines of the file 'with_loop.txt' into a list called 'data',
# and then prints each line one by one along with the last line.
'''
fo=open("with_loop.txt","r")
data=fo.readlines()
fo.close()

for each in range(3):
	print(data[each])   #data[0], data[1],data[2]

print(data[-1])
'''
