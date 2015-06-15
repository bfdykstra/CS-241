#Author: Ben Dykstra
#lab 3
#FB:You need a docstring for this module!
from linearset import Set

class DisjointSet:
    """A class that represents a collection of sets that are disjoint. This 
    means that none of the subsets share any common elements."""
    
    
    def __init__(self):
        # Initializes a disjoint set using a linear set.
        
        self._BigSet = Set()
        
        
    def __len__(self):
        # Returns the total number of elements in all subsets of the 
        # disjoint-set. Accessed using the global Python len() function.
        
        count = 0
        for subset in self._BigSet:
            count += len(subset)
        
        return count
    
    
    def __contains__(self, element):
        # Determines if an element is in the disjoint set. If it is, the method
        # returns True and if not False. Takes the element as a parameter.
        
        for subset in self._BigSet:
            if element in subset:
                return True
        else:
            return False
    
    
    def add(self, element):
        """Creates a new subset whose only member is the element and add the 
        subset into the disjoint-set. The element cannot already be in the 
        disjoint set. Takes an element to be added as a parameter."""
        
        assert element not in self, "The element cannot already be in the set"
       
        newSet = Set()
        newSet.add(element)
    
        self._BigSet.add(newSet)
        
        
    def remove(self, element):
        """Removes the element from its subset. If the subset becomes empty, 
        removes the subset as well.  The element must already be in the 
        disjoint-set. Takes the element to be removed as a parameter."""
        
        assert element in self, "The element must be in the set."
        
        for item in self._BigSet:
            if element in item:
                item.remove(element)
                if len(item) == 0:
                    self._BigSet.remove(item)
                    
                
    def union(self, element1, element2):
        """If the two elements do not belong to the same subset, 
        a union operation is performed over the two subsets. The two subsets 
        that the elements belonged to are then removed and the elements placed
        into a single subset. Takes two elements from different subsets
        as parameters."""
       
        assert (element1 in self) and (element2 in self), "The elements \
        must already be in the disjoint set."
        
        
        subset1 = self.subset(element1)
        subset2 = self.subset(element2)
        
        if subset1 == subset2:
            pass
        else:
            self._BigSet.remove(subset1)
            self._BigSet.remove(subset2)
                
            newSet = subset1.union(subset2)
            self._BigSet.add(newSet)
        
        
    def subset(self, element):
        """Returns the subset the element belongs to. The element must already 
        be in the disjoint-set. Takes an element as a parameter."""

        assert element in self, "element must be in the disjoint set"
        
        for subset in self._BigSet:
            if element in subset:
                return subset
            
    
    def __str__(self):
        """Returns a formatted string that is called when the print() function 
        is called."""
        
        mystr = ""
        for subset in self._BigSet:
            mystr += "{"
            for item in subset:
                mystr +=    str(item) +  ","
            mystr += "}"
        return "{" + mystr + "}"
        
        
        
        
