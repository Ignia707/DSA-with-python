"""
Question:

Given a string, count how many times each character appears using a dictionary.
"""

Input = "aabbbc"

def freq (input):
  freq_dict = {}

  for char in input:
    freq_dict[char] = freq_dict.get(char, 0) + 1
  return freq_dict

print(freq(Input))


# ! know the difference between .get() and .setdefault() clearly