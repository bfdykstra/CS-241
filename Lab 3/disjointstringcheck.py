# ----------------------- TEST SUITE ----------------------------

from disjointset import DisjointSet
from linearset import Set


def main():
	disj1 = DisjointSet()
	disj1.add("a")
	disj1.add("c")
	disj1.add("b")

	disj2 = DisjointSet()
	disj2.add("c")
	disj2.add(["a","b","c"])


	
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
		disj1.union("a","c")
		print(disj1)
		if len(disj1) != 3:
			raise ValueError()
		else:
			print("%20s %20s" % ("TEST union()", "PASSED"))

		# test subset()
		print("Testing subset()")
		testSet = Set()
		testSet.add("c")

		if testSet == disj2.subset("c"):
			print("%20s %20s" % ("TEST subset()", "PASSED"))
		else:
			raise ValueError()

		 
	except ValueError:
		print("TEST FAILED")



main()