#author: Ben Dykstra
#lab 7

# An ADT that implements a deque data structure using a python list. It is 
# a linear collection that supports item insertion and removal at both ends.

class MyDeque:

	
	def __init__(self):
		"""Creates an empty queue"""

		self._dqList = list()

	
	def isEmpty(self):
		"""Returns True if the deque is empty"""

		return len(self) == 0


	def __len__(self):
		"""Returns the number of items in the deque."""

		return len(self._dqList)

	def addFirst(self, item):
		"""Inserts the item at the front of the deque."""

		self._dqList.insert(0, item)


	def addLast(self, item):
		"""Inserts the item at the back of the deque."""

		self._dqList.append(item)


	def removeFirst(self):
		"""Removes and returns the first item of the deque. The deque cannot 
		be empty."""

		assert not self.isEmpty(), "Cannot remove from an empty deque."

		#item = self._dqList.pop(0)

		return self._dqList.pop(0)


	def removeLast(self):
		"""Removes and returns the last item of the deque. The deque cannot 
		be empty."""

		assert not self.isEmpty(), "Cannot remove from an empty deque."

		return self._dqList.pop()

	def peekFirst(self):
		"""Returns but does not remove the first item of the deque. If the 
		deque is empty, returns None."""

		if self.isEmpty():
			return None

		return self._dqList[0]


	def peekLast(self):
		"""Returns but does not remove the last item of the deque. If the
		deque is empty, returns None."""

		if self.isEmpty():
			return None

		lastNdx = len(self._dqList) - 1

		return self._dqList[lastNdx]






	