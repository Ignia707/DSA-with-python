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


"""
# ! If you were asked to solve this without using .most_common(k) (i.e., implementing the mechanism yourself to meet the complexity constraint), you would typically use a method called Bucket Sort or Quickselect.Objective: Achieve $O(N)$ time complexity.Method (Bucket Sort): After counting the frequencies (which is $O(N)$), you can create an array (the "buckets") where the index represents the frequency, and the value is a list of numbers that have that frequency. Since the maximum frequency is $N$, the bucket array size is $N+1$. You then iterate the buckets backward to find the top $k$ elements.
"""