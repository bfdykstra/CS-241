#glist test code

from glist import GList
from glist import _ListNode

myList = GList()
myList.append(1)
myList.append("a")
myList.append("b")
myList.append("z")
myList.append("b")



print(myList._head.data)
print(myList._cur.data)
print(myList._tail.data)


print("The current pointer should now be 'b' and is at the end of the list: ", \
      myList.get())
print("Testing the findNext method, should return False: ", \
      myList.findNext("b"))
print("The first item in myList should be 1: ", myList.getFirst())
print("The current pointer is now at the beginning:  ", myList.get())
print("The next node in the list should be 'a': ", myList.getNext())
print("The next node in the list should be 'b': ", myList.getNext())
print("The next node in the list should be 'z': ", myList.getNext())
print("The current pointer is now: ", myList.get())
print("Now we're at the end of the list: ", myList.getLast())
print("The previous data item is supposed to be 'z': ", myList.getPrevious())
print("testing the findPrevious method for the letter 'a',: ", \
      myList.findPrevious("a"))
#print("testing the findPrevious method for the letter 'x',: ", \
      #myList.findPrevious("x"))
print("Reset current pointer to 1: ", myList.getFirst())
#print("testing to see if findNext method includes the current item: ", \
      #myList.findNext(1)) 
print("the current pointer is now: ", myList.get())
print("Testing to see if getPrevious sets current pointer to None if at \n"
"beginning of list: ", myList.getPrevious())
print("the current pointer is now: ", myList.get())
print("put pointer at end of the list: ", myList.getLast())
print("dialing back pointer to 'z' in order to test insert next: ", \
      myList.getPrevious())
myList.insert(2)
print("the pointer should now be 2: ", myList.get())
print(myList.getPrevious())
print(myList.getNext())
print(myList.getNext())


