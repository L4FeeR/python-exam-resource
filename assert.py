"""
1.Use to check the an return value, basically a debugging tool or checker implemented by developer/programmer <ourslef>
2.It raise assertion error if the expression not satified for a specific value!

SYNTAX :

	assert expression[args]

"""

#eg:

def even_conv(x):
	if x%2==0:
		return x
	else:
		f=x//2
		g=f+f
		return g

print(even_conv(25))
assert even_conv(25)==24, "Wrong!, 24 expected"

print("First example done \n\n")
#Here in this above code, no assertion is raised as 25 as input exactly give 24, so no error in answer/return value

print("Second Example")

assert even_conv(15)==34, "Assertion is always possible for this wrong value"

#Here , as the above line return 14, but assertion is checked for 34, the assertion error occurs as expected value is 34, <thats we provided to check>


"""

by setting an variable in linux by running this command :
	
	export PYTHONOPTIMIZE=1
		-the assert will work, the code runs witn checkign assert syntax line
	export PYTHONOPTIMIZE=0
		-the assert wont work, simply code runs without checkin assert syntax line, in other words : debugging is disabled <assert is debugging tool>

"""
