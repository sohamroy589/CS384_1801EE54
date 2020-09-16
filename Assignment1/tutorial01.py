# Function to throw an error when invalid types are used in the operations
def throw_error():
	print("Error: Invalid Operation!")

# Function to check the type of the variable
def type_check(num):
	if type(num) == int or type(num) == float:
		return True
	return False

# Function to add two numbers 
def add(num1, num2): 
	if not (type_check(num1) and type_check(num2)):
		throw_error()
		return 0
	addition = num1 + num2
	return addition

# Function to subtract two numbers 
def subtract(num1, num2): 
	if not (type_check(num1) and type_check(num2)):
		throw_error()
		return 0
	subtraction = num1 - num2
	return subtraction

# Function to multiply two numbers 
def multiply(num1, num2): 
	if not (type_check(num1) and type_check(num2)):
		throw_error()
		return 0
	multiplication = num1 * num2
	return multiplication

# Function to divide two numbers 
def divide(num1, num2): 
	if not (type_check(num1) and type_check(num2)):
		throw_error()
		return 0
	if num2 == 0:
		print("Can't divide by zero!")
		return 0
	division = num1 / num2
	return division


# Function to add power function
#You cant use the inbuilt python function x ** y . Write your own function
def power(num1, num2): #num1 ^ num2
	if not (type_check(num1) and type_check(num2)):
		throw_error()
		return 0
	power = 1
	while num2 > 0:
		if num2 & 1:
			power *= num1
		num1 *= num1
		num2 >>= 1
	return power
	
# Python 3 program to print GP.  geometric Progression
#You cant use the inbuilt python function. Write your own function
def printGP(a, r, n): 
	gp=[]
	for i in range(n):
		if i == 0 : gp.append(a)
		else:
			gp.append(multiply(gp[-1], r))
	return gp 

# Python 3 program to print AP.  arithmetic Progression
#You cant use the inbuilt python function. Write your own function
def printAP(a, d, n): 
	ap=[]
	for i in range(n):
		if i == 0 : ap.append(a)
		else:
			ap.append(add(ap[-1], d))
	return ap

# Python 3 program to print HP.   Harmonic Progression
#You cant use the inbuilt python function. Write your own function
def printHP(a, d, n): 
	hp=[]
	return hp
	