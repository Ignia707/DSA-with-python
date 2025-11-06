"""
Question:

Design a simple Hit Counter. The counter will be initialized and capable of recording timestamps for hits and returning the total number of hits in the past 5 minutes (300 seconds)


"""
from collections import deque, Counter

class TimeStampError(Exception):
  def __init__(self, message="Timestamp must be ahead of earlier log"):
    super().__init__(message)

class HitCounter:
  def __init__(self):
    self.queue = deque([])

  def __len__(self):
    return len(self.queue)
  
  def hit(self, timestamp):
    if not self.__len__() or timestamp > self.queue[-1]:
      return self.queue.append(timestamp)

    raise TimeStampError()
  
  def get_hits(self, timestamp):
    while self.queue and self.queue[0] <= timestamp - 300:
      self.queue.popleft()
    
    return self.__len__()

HC = HitCounter()

HC.hit(1)

HC.hit(2)

HC.hit(3)

print(HC.get_hits(4))

HC.hit(300)

print(HC.get_hits(300))
print(HC.get_hits(301))