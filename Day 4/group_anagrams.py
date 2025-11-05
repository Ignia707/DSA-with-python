"""
Question:

Given an array of strings strs, group the anagrams together. You may return the answer in any order.

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

from collections import defaultdict


inputs = [["eat", "tea", "tan", "ate", "nat", "bat"], [""], ["a"]]

# [values for _, values in words.items() if len(values) > 0]

  # if len(input) < 2:
  #   return [[input[0]]]


def group_anagrams (input):
  words = defaultdict(list)
  
  for word in input:
    canon_key = "".join(sorted(cleaner(word)))
    
    if word not in words[canon_key]:
      words[canon_key].append(word)
  
  return list(words.values())

def cleaner (input):
  return input.strip().lower()

for input in inputs:
  print(group_anagrams(input))

"""
Corrections:

1. Key for checking use the canon key -> because the code is trying to store generalized key in dicts, if you check it with every word as key then empty lists come up in defaultdict
2. deafultdict handles -> empty inputs and single input cases (whenever it sees a new key it initializes it)
"""