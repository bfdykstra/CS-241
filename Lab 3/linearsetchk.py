from linearset import Set

# -------------------------------------- TEST SUITE-----------------------------

# test constructor
setA = Set()
setB = Set()
setC = Set()
# TEST 1
try:
	# test len()
	if len(setA) != 0:
		raise ValueError()
	
except ValueError:
	print("TEST 1 FAILED")
else:
	print("TEST 1 PASSED")

# TEST 2
try:
	# test add()
	setA.add(["a", 1])
	setA.add("STRING")
	setA.add(10)

	# test len()
	if len(setA) != 3:
		raise ValueError()

	# test __contains__()
	if ("STRING" not in setA) or (10 not in setA):
		raise ValueError()

	# test remove()
	setA.remove(10)
	if len(setA) != 2:
		raise ValueError()

	# test iterator
	print("Should print out: ['a', 1] and STRING")
	for item in setA:
		print(item)

except ValueError:
	print("TEST 2 FAILED")
else:
	print("TEST 2 PASSED")

# TEST 3
try:
	setA.add(["a", 1])
	setA.add("STRING")
	setB.add(["a", 1])
	setB.add("STRING")
	
	#test __eq__()
	if setA == setB:
		pass
	else:
		raise ValueError()

	#test isSubsetOf()
	setA.add(10)
	if setB.isSubsetOf(setA) != True:
		raise ValueError()
	
	#test union()
	setB.add(0)
	setC = setA.union(setB)
	#for item in setC:
		#print(item)
	if len(setC) != 4:
		raise ValueError()	

except ValueError:
	print("TEST 3 FAILED")
else:
	print("TEST 3 PASSED")

# TEST 4
try:
	setA.clear()
	setB.clear()
	setC.clear()
	setA.add([1])
	setA.add("S")
	setA.add(2)
	setB.add("S")
	setB.add([1])
	setB.add(3)
	
	# test intersect()
	setC = setA.intersect(setB)

	if len(setC) != 2:
		raise ValueError()
	
	# test difference()
	
	setA.clear()
	setB.clear()
	setC.clear()
	setA.add(1)
	setA.add("STRING")
	setA.add(0)
	setB.add(2)
	setB.add(1)
	setB.add("JK")
	
	setC = setA.difference(setB)
	
	#for item in setC:
		#print(item)
	if len(setC) != 2:
		raise ValueError()
	
except ValueError:
	print("TEST 4 FAILED")
else:
	print("TEST 4 PASSED")
	