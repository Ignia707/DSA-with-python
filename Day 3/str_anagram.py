"""
Question:

Two strings are anagrams if they contain the same characters with the same frequency, just in different orders.

Example: "listen" and "silent" → both have same letters {l, i, s, t, e, n} with same counts.
"""

str1 = "listen"
str2 = "silent"

def is_anagram (str1, str2):
  
  if (len(str1) !=  len(str2)) or (freq(str1) != freq(str2)):
    return False
  
  
  return True

# * reused the function from freq_dict
def freq (input):
  freq_dict = {}

  for char in input:
    freq_dict[char] = freq_dict.get(char, 0) + 1
  return freq_dict

print(is_anagram(str1, str2))

# ! collections approach

from collections import Counter

def is_anagram_ (input1, input2):
  if (len(input1) != len(input2)) or (Counter(input1) != Counter(input2)):
    return False
  
  return True

print(is_anagram_(str1, str2))
