#Basic FILE HANDLING

"""ASSUME FILE test.txt

hello there
it was fun
"""




#No need to import anything, but sys is fine for checking file present or not!

#1.Initialising file to a variable
#Syntax : open(FILE_NAME, MODE)
file=open("test.txt", "r")

#2.Reading a file
f=open("test.txt", r")
for x in f:
	print(x)
"""
Here in the above code, x simply returns every line one by one for every iteration
To put it simply, f variable contains contents inside the file, if we iterate the variable,it iterates line one by one. 
just assume everyline is array, like [line1, line2, line3]


funtions def : 

1.readline : it simply save one line from file, dpends on where the cursor is there, 

2.readlines : it simply save the content inside file into a variable as list, sepearted by one by one line with '\n'
eg : 
r=f.readlines() 
print(r)
f.close()
#output : ['hello there\n', 'it was fun\n']







"""

#3.Writing to a file

f=open("test.txt", 'w')
f.write("single line is writed unless \n is used to seperate lines")
f.close()

#even when u write multiple time, it appe ds in same line , so use \n or list method
#another example
f=open("test.txt", 'a+')
f.writelines(["lastline\n","next to lastline"])
f.close()

#4.Append

file = open('test.txt', 'a')
file.write("This will add this line at end")
file.close()


#With syntax
''''using this with statement, there is no need to close file manually using close(), it closes when statement ends'''
"""SO memory and code is become efficient!"""

with open("test.txt", 'a+') as f:
	f.read()



"""
------------
FILE MODES
	
	a  : append, wihtout removing text which already present in file
	w  : writing, using this will clear previous content present in file, and latest written only present!
	b  : used for working with binary files, such as images, audio files, etc. It’s often combined with read (`’rb’`) or write (‘wb’) modes.
	r+ : allow to read and write without truncate (not like w)
	w+ : This mode is similar to ‘r+’, but it also truncates the file, removing its existing contents..
-------------
Seek Fnction :

	when accessing file content seek plays an importnat role,
	u should seek to zeroth byte to perform reading multiple time perfectly
	just use seek(0) inbetween every two same operation like readline, readlines,..

	actually it have two paramter, seek(1st, 2nd)
	1st param u know, secon paramis just tell the cursor to be in 'start', 'end', 'current' postion
	we can use both to manipulate the cursor postion,
eg : 
	seek(-2, 2)
here 2nd param 2 reprsent eof, -2 says two letter before the end of file.hope u understood :)
------------- 
Tell Function :

	it reeturns where the cursor is currentlty there,
	it greatly helps when using with seek, just think urself how we can use this, u will surely get it.
	clue: by knowing current postion, u can manipulate the cursor to somewhere u need
	SYNTAX: f.tell()
	eg:
		f.seek(0)
		print(f.tell()) #0 as output
-------------
