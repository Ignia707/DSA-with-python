"""
Question:

Given a string s, find the "first" non-repeating character in it and return its index. If it does not exist, return -1

! NOTE: here in the Counter dict (Python 3.7+) the order of keys is same as the first occurence of those keys in the string (in this case)
"""

from collections import Counter

s = "aabb"

def non_rep(input):
  freq = Counter(input)
  
  for key, value in freq.items():
    if value == 1:
      return input.index(key) # * to get index of char from string, be used for list as well
  
  return -1

print(non_rep(s))