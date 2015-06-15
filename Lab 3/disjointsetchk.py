# ----------------------- TEST SUITE ----------------------------

from disjointset import DisjointSet
from linearset import Set


def main():
	disj1 = DisjointSet()
	disj1.add(1)
	disj1.add(3)
	disj1.add(2)

	disj2 = DisjointSet()
	disj2.add(3)
	disj2.add([1,2,3])


	
	disj3 = DisjointSet()

	print(disj1)
	print(disj2)

	try:
		# test len()
		print("Testing len()...")
		if (len(disj1) != 3) or (len(disj2) != 2):
			raise ValueError()
		else:
			print(" %20s %20s " % ("TEST len()", "PASSED"))

		# test union()
		print("Testing union()...")
		disj1.union(1,3)
		print(disj1)
		if len(disj1) != 3:
			raise ValueError()
		else:
			print("%20s %20s" % ("TEST union()", "PASSED"))

		# test subset()
		print("Testing subset()")
		testSet = Set()
		testSet.add(3)

		if testSet == disj2.subset(3):
			print("%20s %20s" % ("TEST subset()", "PASSED"))
		else:
			raise ValueError()

		 
	except ValueError:
		print("TEST FAILED")



main()