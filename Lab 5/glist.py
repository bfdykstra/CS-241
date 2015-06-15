#Author: Ben Dykstra
#Lab 5


#FB: Docstring!
class GList:
    """An ADT that implements a generic linked list."""
    
    def __init__(self):
        self._head = None
        self._tail = None
        self._cur = None
        self._size = 0


    def __len__(self):
        """Returns size of the list"""
        
        return self._size


    def __contains__(self, item):
        """Returns whether item is in the list. Takes in that item as a 
        parameter."""

        curNode = self._head
        while curNode is not None and curNode.data != item:
            curNode = curNode.Next
            self._cur = curNode #ADD
        return curNode is not None
    #FB: You should set your current node!

    def append(self, item):
        """appends an item to the end of the list. Takes in an item as 
    a parameter"""

        newNode = _ListNode(item)
        if self._head is None:
            self._head = newNode
            self._cur = newNode
            self._tail = newNode
            self._cur.prev = None
            self._cur.Next = None

        else:
            self._cur.Next = newNode
            self._tail = newNode
            newNode.prev = self._cur
            
        self._cur = newNode  #always sets the current pointer to the newNode
        self._size += 1


    def clear(self):
        """Clears all nodes from the list."""
        
        self._head = None
        self._tail = None
        self._cur = None
        self._size = 0


    def findNext(self, item):
        """Finds the next occurence of the item from the current position and 
        returns True/ False if the item is found. Takes in the item to be found 
        as a parameter."""

        assert self._cur is not None

        while self._cur.Next is not None:
            #if self._cur.Next.data is item:
            if self._cur.Next.data is item:
                self._cur = self._cur.Next
                return True
            else:
                self._cur = self._cur.Next

        self._cur = None
        return False


    def findPrevious(self, item):
        """Finds a previous occurence of the item in the list from the current
        position and returns True/False if the item is found. Takes in the item
        as a parameter."""

        assert self._cur is not None

        while self._cur.prev is not None:
            if self._cur.prev.data is item:
                self._cur = self._cur.prev
                return True
            else:
                self._cur = self._cur.prev

        self._cur = None
        return False
    

    def get(self):
        """Returns the current Node"""
        
        if self._cur is None:
            return None
        
        return self._cur.data


    def getFirst(self):
        """Returns the first node of the list."""
    #FB: What if head is None?
        myVal = self._head.data
        self._cur = self._head
        return myVal

  
    def getLast(self):
        """Returns the last node of the list."""
    #FB: What if tail is None?
        myVal = self._tail.data
        self._cur = self._tail

        return myVal


    def getNext(self):
        """Returns the next node in the list."""
    
        assert self._cur is not None

        myVal = self._cur.Next
        self._cur = self._cur.Next
        if myVal is None:
            return None
        
        return myVal.data
    

    def getPrevious(self):
        """Returns the previous node in the list."""

        assert self._cur is not None
    
        myVal = self._cur.prev
        self._cur = self._cur.prev
        if myVal is None:
            return None
        
        return myVal.data


    def insert(self, item):
        """Inserts an item at the current location in the list. Takes in that
        item as a parameter."""

        assert self._cur is not None

        newNode = _ListNode(item)
        
        if self._cur is self._head:
            self.prepend(newNode)

        else:
            
            newNode.prev = self._cur.prev
            newNode.Next = self._cur
            
            self._cur.Next = newNode
            self._cur.prev = newNode

        self._cur = newNode
        self._size += 1 
        
    
    def prepend(self, item):
        """Inserts node at the beginning of the list. Takes in a data item
        as a parameter"""
        
        newNode = _ListNode(item)

        if self._head is None:
            self._head = newNode
            self._cur = newNode
            self._tail = newNode
            self._cur.prev = None
            self._cur.Next = None

            self._cur.Next = newNode
            self._tail = newNode
            newNode.prev = self._cur    
        else:
            newNode.Next = self._head
            newNode.prev = None
            self._cur.Next = newNode
            self._head.prev = newNode
            self._head = newNode
            
            
        self._cur = newNode  #always sets the current pointer to the newNode
        self._size += 1        


    def remove(self):
        """Removes the current node from the list."""

        assert self._cur is not None
        
        if self._cur.Next is None and self._cur.prev is None:
            self._cur.clear() #FB: I don't understand this line
            
        elif self._cur.Next is None:
            tempPrev = self._cur.prev
            self._cur.prev.Next = None
            self._tail, self._cur = tempPrev, tempPrev
            
        elif self._cur.prev is None:
            tempNext = self._cur.Next
            self._cur.Next.prev = None
            self._head, self._cur = tempNext, tempNext
        
        else:
            oldPrev = self._cur.prev
            self._cur = self._cur.Next
            oldPrev.Next = self._cur
            self._cur.prev = oldPrev
            
        self._size -= 1



class _ListNode:
    """A storage class that takes in any data item as a parameter."""
    def __init__(self, data):
    
        self.data = data
        self.Next = None
        self.prev = None
