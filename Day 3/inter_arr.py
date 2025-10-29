"""
Question:

Given two lists (arrays), return a list of unique elements that appear in both.
"""

arr1 = [1, 2, 2, 3, 4]
arr2 = [2, 2, 4, 6]

def func (arr1, arr2):
  # * here you are returning as "set" datatype - do mind it
  return set(arr1) & set(arr2)

print(list(func(arr1, arr2)))