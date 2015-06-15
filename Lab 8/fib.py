#Author: Ben Dykstra
#Lab 8: Recursion

"""An implementation of a non-recursive and recursive fibonacci sequence. 
The main() function tests those functions.
"""

import time

def main():
	""" Main function that tests the recursive and non-recursive fibonacci functions. It compares
	their speed by using the time function. """
	
	#n = int(input("Enter n: "))
	n = 22
	print()
	
	t0 = time.time()
	f1 = fib1(n)
	print("fib1(%d) = %d" % (n, f1))
	t1 = time.time()
	print("fib1 elapsed time is %5.3f." % (t1-t0))
	
	print()

	t0 = time.time()
	f2 = fib2(n)
	print("fib2(%d) = %d" % (n, f2))
	t1 = time.time()
	print("fib2 elapsed time is %5.3f." % (t1-t0))
	
	print()

	if f1 != f2:
		print("Test failed!")

	print()
	
	printFibHistogram(11)

def fib1(n):
	""" A non-recursive implementation of the fibonacci sequence."""
	
	assert n >= 0, "Fibonacci not defined for n < 0"
	if n == 1 or n == 0:
		return n

	else:
		x_1 = 1
		x_2 = 1
		for i in range(n - 1):
			total = x_1 + x_2
			x_1 = x_2
			x_2 = total
			
	return x_1

	

def fib2(n):
	""" A recursive implementation of the fibonacci sequence. Taken from textbook
	page 283. """

	assert n >= 0, "Fibonacci not defined for n < 0."
	
	if n == 0 or n == 1:
		return n

	else:
		return fib2(n - 1) + fib2(n - 2)


def printFibHistogram(n):
	""" A function that prints out a histogram of fibonacci numbers. """
	
	for i in range(n):
			print('*' * fib1(i+1))
	 
	print("\nCheck the above and below histogram to see if they are identical")
	print("Otherwise, something is wrong!\n")

	for i in range(n):
			print('*' * fib2(i+1))

main()
