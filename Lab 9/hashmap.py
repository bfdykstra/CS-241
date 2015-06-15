#Author: Ben Dykstra
#Lab 09


"""An ADT that implements a HashMap using an underlying array. Similar to a 
dictionary, a key is associated with a value. Uses linear probing to find empty 
spots. This file also contains a private MapEntry class and a HashIterator class. 
The MapEntry class is a storage class implemented to store key and value pairs. 
The HashIterator class is used to traverse the elements of the hash map.

I added string functions to assist in visualization of the underlying structure.
"""


#-----------------------------------------------------------------------------#
#Begin Code


from arrayadt import Array

#Storage class for holding the key/value pairs.
class _MapEntry:
	def __init__(self, key, value):
		self.key = key
		self.value = value

	def __str__(self):
		theKey = str(self.key)
		theValue = str(self.value)

		return "{" + theKey + ": " + theValue + "}"
	

# Implementation of the Map ADT using closed hasing and a linear probe with 
# double hashing

class HashMap:
	
	#defines constants to represent the status of each table entry.
	UNUSED = None #for an unoccupied slot in the array
	EMPTY = _MapEntry(None, None) #marks an entry that has been deleted 

	# Creates an empty map instance
	def __init__(self):
		self._table = Array(7)
		self._count = 0
		self._maxCount = len(self._table) - len(self._table)//3


	# Returns the number of entries in the map
	def __len__(self):

		return self._count

	
	# Returns a string representation of the HashMap
	def __str__(self):
		
		totalString = ""
		for i in self._table:
			totalString += str(i) + ", "
					
		return totalString


	# Determines if the map contains the given key. Takes in a key as a 
	# parameter. Returns True if the value at the key is not None, False 
	# otherwise.
	def __contains__(self, key):

		slot = self._findSlot(key, False)
		
		return self._table[slot] is not None


	# Adds a new entry to the map if the key does not exist. Otherwise, the 
	# new value replaces the current value associated with the key. Takes 
	# in a key and value as parameters. 
	def add(self, key, value):

		if key in self:
			slot = self._findSlot(key, False) #not for insertion
			self._table[slot].value = value
			return False
		else:
			slot = self._findSlot(key, True) #for insertion
			self._table[slot] = _MapEntry(key, value)
			self._count += 1
			if self._count == self._maxCount:
				self._rehash()
			return True


	# Returns the value associated with the key. Takes in a key as a 
	# parameter. 
	def valueOf(self, key):
		
		slot = self._findSlot(key, False)

		assert slot is not None, "Invalid map key."
		
		if self._table[slot] is None:
			return None
		else:
			return self._table[slot].value


	# Removes the entry associated with the key. Takes in that key value
	# as a parameter.
	def remove(self, key):
		
		assert key in self, "Invalid key."

		#key = self._findSlot(key,False) #FB: I added this line
		self._table[key] = self.EMPTY
		self._count -= 1


	# Returns an iterator for traversing the keys in the map.
	def __iter__(self):
	
		return _HashIterator(self._table)


	# Find the slot containing the key or where the key can be added.
	# forInsert indicates if the search is for an insertion, which locates
	# the slot into which the new key can be added. Takes in a key and a 
	# boolean for the forInsert parameter. Returns a slot
	def _findSlot(self, key, forInsert):
		
		# Compute the home slot and set the step size.
		slot = self._hash1(key)
		step = 1
		 
		# Probe for the key
		M = len(self._table)
		while self._table[slot] is not None:
			if forInsert and \
				(self._table[slot] is self.UNUSED or self._table[slot] is self.EMPTY):
				return slot

			elif not forInsert and \
				(self._table[slot] is not self.EMPTY and self._table[slot].key == key):

				return slot
			else:
				slot = (slot + step) % M

		return slot
		

	# Rebuilds the hash table
	def _rehash(self):
		
		# Create a new larger table.
		origTable = self._table
		newSize = len(self._table) *2 + 1
		self._table = Array(newSize)

		# Modify the size attributes
		self._count = 0
		self. _maxCount = newSize - newSize // 3

		# Add the keys from the original array to the new table.
		for entry in origTable:
			if entry is not self.UNUSED and entry is not self.EMPTY:
				slot = self._findSlot(entry.key, True) 
				self._table[slot] = entry
				self._count += 1


	# The main hash function for mapping keys to table entries. Takes a key
	# in as a parameter. Returns a remainder
	def _hash1(self, key):
	
		return abs(hash(key)) % len(self._table)


	# The second hash function used with double hashing probes. Takes a key 
	# in as a parameter. Returns a remainder
	def _hash2(self, key):
		
		return 1 + abs( hash(key)) % (len(self._table) - 2)


# Iterator class for traversing the values of the hashmap. Returns the keys
class _HashIterator:

	def __init__(self, Array):

		self._arrayRef = Array
		self._curNdx = 0

	def __iter__(self):

		return self
	
	# Will not return a key that has an UNUSED or EMPTY value
	def __next__(self):
		
		size = len(self._arrayRef)
		
		while self._curNdx < size:
			entry = self._arrayRef[self._curNdx]
			
			if entry is (HashMap.UNUSED) or (entry is HashMap.EMPTY):
				self._curNdx += 1
			else:
				self._curNdx += 1
				return entry.key
	
		raise StopIteration
		
	

def main():

	hMap = HashMap()
	
	hMap.add(0, "a")
	print(0 in hMap)
	
	print(hMap.valueOf(0))
	hMap.add(1, "b")
	
	
	hMap.add(3, "d")
	hMap.add(4, "e")
	hMap.add(5, "f")
	hMap.add(6, "g")
	hMap.add(7, "h")

	print(hMap)
	print(hMap.valueOf(7))
	
	
	print(len(hMap))
	hMap.add(8, "i")
	print(hMap)
	hMap.add(9, "j")
	print(hMap)
	for i in hMap:
		print(hMap.valueOf(i))
		
	hMap.remove(4)
	hMap.remove(6)
	
	print(hMap)
	hMap.add(4, "e")
	print(hMap)
	print(9 in hMap)
		
main()


