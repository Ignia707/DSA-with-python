from collections import deque

class Queue:
  def __init__ (self):
    self.queue = deque([])

  def enqueue (self, value):
    self.queue.append(value)

  def dequeue (self):
    # try:
      return self.queue.popleft() # ! when index out of range it is handled and thrown python
    
    # except IndexError:
    #   print("Index error")
    #   return -1

  def peek (self):
    if self.is_empty():
      raise IndexError("Cannot peek from an empty queue")
    return self.queue[0]
  
  def __len__ (self):
    return len(self.queue)
  
  def is_empty (self):
    return bool(not self.size())


Q = Queue()

# Q.enqueue('A')
# Q.enqueue('B')

# print(Q.dequeue())

# Q.enqueue('C')

# print(Q.dequeue())
# print(Q.size())
# print(Q.is_empty())

Q.peek()

"""
Lessons to learn:

* Refracts ideas:
? 1. For edge cases or exception inducing code, either re-raise it try-except blocks or let the python handle it (normal errors thrown  by it) or raise a custom error
? 2. Use __len__() for returning size -> kinda inbuilt so use that
? 3. `bool(not self.size())` -> `not self.size`  is enough

"""