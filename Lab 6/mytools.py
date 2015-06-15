#Lab 6
#Author: Ben Dysktra

from lstack import Stack
import math

# This program includes three functions. The first one converts an integer 
# into a string and returns that string. The second and third functions
# evaluate a postfix or prefix expression and return a real number.
#------------------------------------------------------------------------#


#Begin Code

def mystr(anInteger):
	"""A function that converts an integer into a string using a stack. 
	Takes an integer as a parameter."""
		
	myStack = Stack()

	if anInteger == 0:
		myStack.push(anInteger)

	elif anInteger < 0:
		anInteger = abs(anInteger)
		
		while anInteger != 0:
			rem = anInteger % 10
			myStack.push(rem)
			anInteger = anInteger // 10
		

		totalString = ""
		totalString += "-"
		for i in range(len(myStack)):
			char = chr(myStack.pop() + 48)
			totalString += char

		return totalString

	else:
		while anInteger != 0:
			rem = anInteger % 10
			myStack.push(rem)
			anInteger = anInteger // 10
			


	totalString = ""
	for i in range(len(myStack)):
		char = chr(myStack.pop() + 48)
		totalString += char

	return totalString


def evalPostfix(pfExp):
	"""A postfix expression solver. Takes a postfix expression in the form of a
	text string as a parameter."""

	myStack = Stack()

	exp = pfExp.split()
	operatorList = ["-", "+", "*", "/"]

	for i in range(len(exp)):
		if exp[i] in operatorList:
			operator = exp[i]

			y = myStack.pop()
			assert not myStack.isEmpty(), "Invalid postfix expression"
			x = myStack.pop()

			if operator == "-":
				result = x - y
				myStack.push(result)
			elif operator == "+":
				result = x + y
				myStack.push(result)
			elif operator == "*":
				result = x * y
				myStack.push(result)
			elif operator == "/":
				result = x / y
				myStack.push(result)
			
			
		else:
			operand = float(exp[i])
			myStack.push(operand)

	finalResult = myStack.pop()
	
	if myStack.isEmpty() == False: 
		return None

	return finalResult


def evalPrefix(prefixExpression):
	"""A prefix expression solver. Takes in a prefix expression in the 
	form of a text string as a parameter."""

	myStack = Stack()

	exp = prefixExpression.split()
	exp.reverse()
	operatorList = ["-", "+", "*", "/"]

	for i in range(len(exp)):
		if exp[i] in operatorList:
			operator = exp[i]

			y = myStack.pop()
			assert not myStack.isEmpty(), "Invalid prefix expression"
			x = myStack.pop()

			if operator == "-":
				result = y - x
				myStack.push(result)
			elif operator == "+":
				result = x + y
				myStack.push(result)
			elif operator == "*":
				result = x * y
				myStack.push(result)
			elif operator == "/":
				result = y / x
				myStack.push(result)
			
		else:
			operand = float(exp[i])
			myStack.push(operand)

	finalResult = myStack.pop()
	
	if myStack.isEmpty() == False: 
		return None

	return finalResult
	
