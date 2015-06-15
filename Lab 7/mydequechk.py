from mydeque import MyDeque

dq = MyDeque()

print(dq.isEmpty())

print(len(dq))

dq.addFirst("a")
dq.addLast("b")
dq.addFirst("c")

print("The first item should be c: ", dq.peekFirst())
print("The last item should be b: ", dq.peekLast())

dq.removeFirst()
print("After removing c, the first item should be a: ", dq.peekFirst())

print("The length of the deque should now be 2: ", len(dq))
print(dq.isEmpty())
dq.removeLast()
dq.removeLast()
dq.addLast(1)
dq.addLast("This is a fresh start")
print(dq.peekLast())
print(len(dq))
dq.addFirst("x")
print(dq.peekFirst())
dq.addFirst("lol this lab doe")
print(dq.peekFirst())
