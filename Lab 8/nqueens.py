#Author: Ben Dykstra
#Lab 08

import ctypes
import math

class _Array :
	"""Implementation of a c type array."""
	
	# Creates an array with size elements.
	def __init__( self, size ):
		assert size > 0, "Array size must be > 0" 
		self._size = size
		
		# Create the array structure using the ctypes module.
		PyArrayType = ctypes.py_object * size
		self._elements = PyArrayType()
		
		# Initialize each element.
		self.clear( None )

	 
	 #returns the size of the array.   
	def __len__(self):
		return self._size

	
	#gets the contents of the index element.
	def __getitem__(self, index):
		assert index >= 0 and index < len(self), "Array subscript out of range"
		return self._elements[index]

	
	#puts the value in the array element at index position
	def __setitem__(self, index, value):
		assert index >= 0 and index < len(self), "Array subscript out of range"
		self._elements[index] = value

		
	#clears the array by setting each element to the given value.
	def clear(self, value):
		for i in range(len(self)):
			self._elements[i] = value

			
	#Returns the array's iterator for traversing the elements.
	def __iter__(self):
		return _ArrayIterator(self._elements)
	
	
class _ArrayIterator:
	"""A private class that iterates over a given array."""
	
	def __init__(self, theArray):
		self._arrayRef = theArray
		self._curNdx = 0

		
	def __iter__(self):
		return self

	
	def __next__(self):
		if self._curNdx < len(self._arrayRef):
			entry = self._arrayRef[self._curNdx]
			self._curNdx += 1
			return entry
		else:
			raise StopIteration
		

class _Array2D:
	"""Implementation of the Array2D ADT using an array of arrays."""

	#creates a 2-D array of size numRows x numCols.
	def __init__(self, numRows, numCols):
		#create a 1-D array to store an array reference for each row.
		self._theRows = _Array(numRows)
		
		#create the 1-D arrays for each row of the 2-D array.
		for i in range(numRows):
			self._theRows[i] = _Array(numCols)

			
	#returns the number of rows in the 2-D array.
	def numRows(self):

		return len(self._theRows)

	
	#Returns the number of columns in the 2-D array.
	def numCols(self):

		return len(self._theRows[0])


	#Clears the array by setting every element to the given value.
	def clear(self, value):

		for row in range(self.numRows()):
			self._theRows[row].clear(value)

			
	#gets the contents of the element at position [i,j]
	def __getitem__(self, ndxTuple):

		assert len(ndxTuple) == 2, "Invalid number of array subscripts."
		row = ndxTuple[0]
		col = ndxTuple[1]
		assert row >= 0 and row < self.numRows() and col >= 0 \
			   and col < self.numCols(), "Array subscript out of range."
		the1dArray = self._theRows[row]
		return the1dArray[col]

	
	#Sets the contents of the element at position [i,j] to value.
	def __setitem__(self, ndxTuple, value):
	
		assert len(ndxTuple) == 2, "Invalid number of array subscripts."
	
		row = ndxTuple[0]
		col = ndxTuple[1]
		assert row >= 0 and row < self.numRows() and col >= 0 \
				and col < self.numCols(), "Array subscript out of range." 
		the1dArray = self._theRows[row]
		the1dArray[col] = value


class Board:
	""" A class that represents a chessboard, implemented using a 2D Array.
	Contains a solveNQueens method that recursively finds a solution to
	the nQueens problem."""
	
	def __init__(self, n):
		"""#initializes an empty board using a 2D array"""
	
		assert n >= 4, "No solutions for a board of size n < 4"
	
		self._myBoard = _Array2D(n, n)
		self.BoardClear(" _ ") 
	

	def BoardClear(self, value):
		"""Clears the board and replaces every square with the given value."""

		self._myBoard.clear(value)

	
	def size(self):
		"""Returns the number of squares in the board.""" 
	
		x = self._myBoard.numRows()
		
		return x 
	
   
	def numQueens(self):
		"""iterates through the board by row and then column and checks if that cell
		contains a queen. Returns the number of queens on the board"""	

		count = 0
		#each row
		for i in range(self.size()):
			#each col
			for j in range(self.size()):
				if self._myBoard[i,j] == " Q ":
					count += 1

		return count

  
	def unguarded(self, row, col):
		"""Returns a boolean value indicating if the given square is currently 
		unguarded by any queen on the board"""	
	
		#check the vertical and horizontal
		for space in range(self.size()):
			if space != row and self._myBoard[space, col] == " Q ":
				return False

			else:
				if space != col and self._myBoard[row, space] == " Q ":
					return False
	
		#if the difference between the space that you are checking lands on a 
		#diagnol of the coordinate where a Q is, then it is guarded. 
		for i in range(self.size()):
			for j in range(self.size()):
				if self._myBoard[ i , j] == " Q ":
					if abs(i - row) == abs(j - col):
						return False
			
		return True
	
	
	def placeQueen(self, row, col):
		"""Places a queen on the board at position (row, col)."""
	
		self._myBoard[row, col] = " Q "

	
	def removeQueen(self, row, col):
		"""Removes the queen from position (row, col)."""
		
		self._myBoard[row, col] = " _ "

	
	def reset(self):
		"""Resets the board to its original state by removing all queens
		currently placed on the board. """  
	
		self.BoardClear(" _ ")

  
	def draw(self):
		"""Prints the board in a readable format using characters to represent the 
		squares containing the queens and the empty squares"""    
	
		for i in range(self.size()):
			for j in range(self.size()):
				print(self._myBoard[i, j], end = "")
		
		
			print()

	   
	def solveNQueens(self, board, col):
		"""Solves for N amount of queens. Will enumerate all solutions. Takes a 
		board size and the current column in which we are attempting to place 
		a queen."""
	
		if board.numQueens() == board.size():
			return True
		
		else:
			# Find the next unguarded square within this column
			for row in range(board.size()): 
				if board.unguarded(row,col):
					#place a queen in that square
					board.placeQueen(row, col)
					#continue placing queens in the following columns
					if board.solveNQueens(board, col + 1):
						# We are finished if a solution is found
						return True
					else:
				#No Solution was found with the queen in this square, 
						 #so it has to be removed from the board
						board.removeQueen(row, col)
			#if loop terminates, no queen can be places within this column
			return False


def main():
	userInput = ""
	while userInput != "n":

		print()
		userInput = int(input("Please enter the size of the board: "))
		board = Board(userInput)
		y = board.solveNQueens(board, 0)
		board.draw()
		userInput = input("Would you like to play again? (y/n): ")
		userInput.lower()
		print()

	print("Thanks for playing!")
		
main()

