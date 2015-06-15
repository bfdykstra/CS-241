#Lab 6

"""Implementation of the Stack ADT using a Python List. Taken from textbook
page 196."""

class Stack:
	
	def __init__(self):
		"""Creates an empty stack."""

		self._theItems = list()


	def isEmpty(self):
		"""Returns True if the stack is empty or False otherwise."""

		return len(self) == 0


	def __len__(self):
		"""Returns the number of items in the stack."""

		return len(self._theItems)


	def peek(self):
		"""Returns the top item on the stack without removing it."""

		assert not self.isEmpty(), "Cannot peek at an empty stack"

		return self._theItems[-1]


	def pop(self):
		"""Removes and returns the top item on the stack."""

		assert not self.isEmpty(), "Cannot pop from an empty stack."""

		return self._theItems.pop()


	def push(self, item):
		"""Push an item onto the top of the stack."""

		self._theItems.append(item)

