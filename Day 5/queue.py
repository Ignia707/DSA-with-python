"""
Docstring for Day 5.queue
  Enqueue
  Dequeue
  Peek
  Rear
  Clear
"""

from collections import deque

class Queue:
    def __init__(self):
        self.q = deque()

    def enqueue(self, x):
        self.q.append(x)
        return self.q
    
    def dequeue(self):
        if not self.q:
            return -69
        else:
            return self.q.popleft()
    """
    othes are easy skipped it
    """

que = Queue()
print(que.enqueue(1))
print(que.enqueue(7))
print(que.enqueue(4))

print(que.dequeue())
print(que.q)