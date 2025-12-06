"""
Docstring for Day 7.max_heap
Max-heap using negative values
"""

import heapq

class max_heap():
  def __init__(self):
    self.heap = []

  def push(self, x):
    heapq.heappush(self.heap, -x)
    return self.heap
  
  def pop(self):
    popped = -heapq.heappop(self.heap)
    return popped
  
mheap = max_heap()

mheap.push(10)
mheap.push(4)

print(mheap.pop())  # 10

mheap.push(20)
mheap.push(15)

print(mheap.pop())  # 20
print(mheap.pop())  # 15


