

import time

def main():
	n = 5
	print()
    
	t0 = time.time()
	f1 = fib1(n)
	print("fib1(%d) = %d" % (n, f1))
	t1 = time.time()
	print("fib1 elapsed time is %5.3f." % (t1-t0))


def fib1(n):

	""" A non-recursive implementation of the fibonacci sequence."""
	
	assert n >= 1, "fibonacci not defined for n < 1"
	if n == 1:
		return 1

	else:
		x_1 = 1
		x_2 = 1
		for i in range(n - 1):

			total = x_1 + x_2
			x_1 = x_2
			x_2 = total
			
	return x_1

main()

