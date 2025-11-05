from collections import Counter

def topK (nums, k):
  return [key_map[0] for key_map in Counter(nums).most_common(k)]

print(topK([1, 1, 1, 2, 2, 3], 2))