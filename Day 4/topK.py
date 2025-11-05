"""
Question:

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

* Your solution must be better than O(n logn)
"""

from collections import Counter

inputs = [[[1, 1, 1, 2, 2, 3], 2], [[1], 1], [[4, 1, -1, 2, -1, 2, 3], 2]]

def topK (nums, k):
  return [key_map[0] for key_map in Counter(nums).most_common(k)]


for input in inputs:
  print(topK(input[0], input[1]))