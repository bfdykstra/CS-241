#Author: Ben Dykstra
#Lab 02

from arrayadt import Array 


class Vector:
	
	"""A mutable sequence type that works like Python's list structure"""
	
	
	def __init__(self, size = 2):
		"""creates a new empty vector with an initial capacity of two 
		elements."""
		
		#initializes an array that is the size of the input list * 2 to allow for extra
		#spaces
		self._myVect = Array(2)
		self._size = 0
		self._capacity = 2
		 
		
	def __len__(self):
		"""Returns the number of items contained in the vector"""
		
		return self._size
		
	
	def __contains__(self, item):
		"""Returns True if the element is in the vector"""
		
		return item in self._myVect
	
	
	def __getitem__(self, ndx):
		"""Returns the itme stored in the ndx element of the list. The value of 
		ndx must be with the valid range."""
		
		assert ndx >= 0 and ndx <= self._size, "Vector subscript out of range"
		
		return self._myVect[ndx]
	
	
	
	def __setitem__(self, ndx, value):
		"""Sets the element at position ndx to contain the given item. The value 
		of ndx must be within the valid range, which includes the first positon 
		past the last item. """                 
		
		assert ndx >= 0 and ndx <= self._size, "Vector subscript out of range"
		
		#creates new array with double the capacity and copies over old list
		#into it
		if ndx == self._size:
			newVect = Array(2 * self._capacity)
			self._capacity = 2 * self._capacity
			for i in range(len(self._myVect)):
				newVect[i] = self._myVect[i]
			self._myVect = newVect 
		
		if ndx == self._size:
			self._size += 1
			
		self._myVect[ndx] = value
		
		 
	def append(self, item):
		"""Adds the given item to the end of the list."""
		
		
		#creates new array with double the capacity and copies over old list
		#into it
		if self._size == self._capacity:
			newVect = Array(2 * self._capacity)
			self._capacity = 2 * self._capacity
			for i in range(len(self._myVect)):
				newVect[i] = self._myVect[i]
			self._myVect = newVect
			
			self._myVect[self._size] = item
			
		else:
			self._myVect[self._size] = item
			
		self._size += 1
		
		
	def insert(self, ndx, item):
		"""Inserts the given item in the element at position ndx. The items in the 
		elements at and following the given position are shifted up to make room 
		for the new item. Ndx must be within the valid range."""
		
		assert ndx >= 0 and ndx <= self._size, "Index must be in range."
		
		#to check if inserting is going to overload the array. If it does, copies over 
		#old vector into a new array with double the size
		if self._size == self._capacity:
			newVect = Array(2 * self._capacity)
			self._capacity = 2 * self._capacity
			for i in self._myVect:
				newVect[i] = self._myVect[i]
				self._myVect = newVect
				
		
		#create dummy vector to copy all the values into
		dummyVect = Array(self._capacity * 2)
		
		for i in range( ndx):
			dummyVect[i] = self._myVect[i]
			
		dummyVect[ndx] = item
		
		#shifts the values
		for i in range(ndx, self._size):
			dummyVect[i + 1] = self._myVect[i]
		
		self._myVect = dummyVect 
		
		self._size += 1
				
	def remove(self, ndx):
		"""Removes and returns the item from the element from the given ndx 
		position. The items in the elements at and following the given position
		are shifted up to close the gap created by the removed item. Ndx must be 
		within the valid range."""
		
		assert ndx >= 0 and ndx <= self._size, "Index must be in range."
		
		#create dummy vector to copy all the values into
		dummyVect = Array(self._capacity * 2)
		
		for i in range( ndx):
			dummyVect[i] = self._myVect[i]
			
		element = self._myVect[ndx]
		
		#shifts the values
		for i in range(ndx, self._size):
			dummyVect[i - 1] = self._myVect[i]
		
		self._myVect = dummyVect 
		
		self._size -= 1        
			  
		return element
	
	
	def indexOf(self, item):
		"""Returns the index of the vector element containing the given item. 
		The item must be in the list"""
		
		assert item in self._myVect, "Item must be in the vector"
		for i in range(self._size):
			if self._myVect[i] == item:
				return i
	
	def extend(self, otherVector):
		"""Extends this vector by appending the entire contents of the 
		otherVector to this vector"""
		
		for i in otherVector._myVect:
			self.append(i)
			
		
	def subVector(self, start, stop):
		"""Creates and returns a new vector that contains a subsequence of the 
		items in the vector between and including those indicated by the given 
		start and stop positions. Both the from and to positions must be within 
		the valid range."""
		
		assert start <= self._size and start >= 0, "From must be within the \
		valid range"
		assert stop <= self._size and stop >= 0, "To must be within the valid range."
		
		#create new vector that will be filled from the other vector using two
		#different indices.
		newVect = Vector()
		i = start
		x = 0
		while i <= stop:
			newVect[x] = self._myVect[i]
			i += 1
			x += 1
	   
		return newVect
			
			
	def __iter__(self):
		return _VectorIterator(self._myVect)
		
class _VectorIterator:
	"""A class that iterates over a given vector."""
	
	def __init__(self, theVector):
			self._vectorRef = theVector
			self._curNdx = 0
			
	def __iter__(self):
		return self
		
	def __next__(self):
		if self._curNdx < len(self._vectorRef):
			entry = self._vectorRef[self._curNdx]
			self._curNdx += 1
			return entry
		else:
			raise StopIteration    
	
	
	
		
	
	
	