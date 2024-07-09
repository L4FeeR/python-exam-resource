"""
try:	to run  a certain lines of code , if there is an error happen then it was sent to expcept block,

except:	if we mention except with error name, only that error is manipulated here, otherwise wihtout mentioing errorname, everyerror is manipulated here

else: this block of line codes run when there is no error happend in try block code, inotherwords, except and else wont run simultaneously together!

finally:	this blobk of line code always run at end of this try-except-else block. normally used to clean up the  objects in try excpet blck , and other purpose too


example:

try:
	x=1
	while x<100000:
		print()
		x+=1
except KeyboardInterrupt:
	print("Ctrl C is pressed!")
else:
	print("WOah u waited that long!")
finally:
	del x
	print("Anyway try-except block finished")

-----
#create own exceptions simple way!
#Inherinting the base Exceptional class to create our own!



class MyOwnError(Exception):
	"Just defining myown error exceotion, so i can use everywhere i wish!"
	pass

			<or>


class MyOwnError(Exception):	pass


x=10
try:
	if x<15:
		raise MyOwnError("X is greater than 15!")
	else:
		print("Done")
except MyOwnError as err:
	print(err)


-----
----

Types Of EXceptionals: 

	AssertionError  :	Raised when an assert statement fails
	EOFError	:	Raised when the input() method hits an "end of file" condition (EOF)
	ImportError 	:	Raised when an imported module does not exist
	IndentationError:	Raised when indentation is not correct
	IndexError 	:	Raised when an index of a sequence does not exist
	KeyError 	:	Raised when a key does not exist in a dictionary
	KeyboardInterrupt: 	Raised when the user presses Ctrl+c, Ctrl+z or Delete
	NameError 	:	Raised when a variable does not exist
	NotImplementedError: 	Raised when an abstract method requires an inherited class to override the method
	RuntimeError 	:	Raised when an error occurs that do not belong to any specific exceptions
	StopIteration 	:	Raised when the next() method of an iterator has no further values
	SyntaxError 	:	Raised when a syntax error occurs
	TabError 	:	Raised when indentation consists of tabs or spaces
	TypeError 	:	Raised when two different types are combined
	ValueError 	:	Raised when there is a wrong value in a specified data type
	ZeroDivisionError:	Raised when the second operator in a division is zero


Difference between Value and Type Error:
 	A TypeError occurs when an operation or function is applied to an object of inappropriate type.

	A ValueError occurs when a built-in operation or function receives an argument that has the right type but an inappropriate value, 
		and the situation is not described by a more precise exception such as IndexError.

	Examples: passing arguments of the wrong type (e.g. passing a list when an int is expected) should result in a TypeError,
		  but passing arguments with the wrong value (e.g. a number outside expected boundaries) should result in a ValueError.


Examples
	1.TypeError:
			myInt = 100
			myStr = "10"
			myResult = myInt / myStr

	2.ValueError:
			num1=10
			num2="TwentyNine"
			print(float(num1))   #10.0
			print(float(num2))   #ValueError
"""
