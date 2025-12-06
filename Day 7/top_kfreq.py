"""
Docstring for Day 7.top_kfreq
Top K frequent elements
"""

from collections import Counter
import heapq

test = [10, 10, 10, 20, 20, 30, 40, 40, 40, 40]
k = 3

def top_k_freq(arr, k):
  freq_dict = Counter(test)
  heap = []

  for key, value in freq_dict.items():
    heapq.heappush(heap, (value, key))

    if len(heap) > k:
      heapq.heappop(heap) 
  
  result = []
  while heap:
    result.append(heapq.heappop(heap)[1])

  return result

print(top_k_freq(test, k))