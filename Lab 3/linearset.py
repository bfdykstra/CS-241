#Modified by: Ben Dykstra
#lab 3

class Set:
    """Implementation of the Set ADT container using a Python list."""
    
    def __init__(self):
        """Creates an empty set instance using an empty list"""
        
        self._theElements = list()
        
        
    def __len__(self):
        """Returns the number of items in the set"""
        
        return len(self._theElements)
    
    def __contains__(self, element):
        """Determines if an element is in the set"""
        
        return element in self._theElements
    
    def add(self, element):
        """Adds a unique element to the set. Takes the element to be added as a 
        parameter"""
        
        if element not in self._theElements:
            self._theElements.append(element)
            
        else:
            print("that element is already in the set")
            
    
    def remove(self, element):
        """Removes an element from the set. The element must be in the set in 
        order to be removed. Takes the element to be removed as a parameter."""
        
        assert element in self._theElements, "The element must be in the set"
        
        self._theElements.remove(element)
        
    
    def __eq__(self, setB):
        """Determines if two sets are equal. Takes another set as a parameter."""
        
        if len(self) != len(setB):
            return False
        else:
            return self.isSubsetOf(setB)
        
    
    def isSubsetOf(self, setB):
        """Determines if this set is a subset of setB. Takes setB as a parameter."""
        
        for element in self:
            if element not in setB:
                return False
        return True
    
    
    def union(self, setB):
        """Creates a new set from the union of this set and setB. Takes setB as a 
        parameter"""
        newSet = Set()
        newSet._theElements.extend(self._theElements)
        for element in setB:
            if element not in self:
                newSet._theElements.append(element)
                
        return newSet
    
    
    def intersect(self, setB):
        """Creates a new set from the intersection of this set and setB. Takes setB as
        a parameter."""
        
        newSet = Set()
        for element in self:
            if element in setB:
                newSet._theElements.append(element)
        
        return newSet
    
    
    def difference(self, setB):
        """Creates a new set from the difference: self set and setB. Takes setB as a 
        parameter."""
        
        newSet = Set()
        newSet._theElements.extend(self._theElements)
        for element in self:
            if element in setB:
                newSet._theElements.remove(element)
                
        return newSet
    
    
    def __iter__(self):
        """Returns an iterator for traversing the list of items"""
        
        return _SetIterator(self._theElements)
    
    def __str__(self):
        
        mystr = ""
        for item in self._theElements:
            mystr += "{" + str(item) + "}" + ","
        return "{" + mystr + "}"
    
    def clear(self):
        
        self._theElements = list()
    
class _SetIterator:
    
    def __init__(self, theSet):
            self._setRef = theSet
            self._curNdx = 0
            
    def __iter__(self):
        return self
        
    def __next__(self):
        if self._curNdx < len(self._setRef):
            entry = self._setRef[self._curNdx]
            self._curNdx += 1
            return entry
        else:
            raise StopIteration    
        
            
            