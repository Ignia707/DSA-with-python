s = "A man, a plan, a canal: Panama"

def norm_anal(input):
  clean_inp = clean(input)
  return (clean_inp, ispal(clean_inp), top_char(clean_inp))

def clean (input):
  return ("".join([char.lower() for char in input if char.isalpha()])).strip()

def ispal (input):
  return (input == input[::-1])

def top_char (input):
  freq = {}

  for char in input:
    freq[char] = freq.get(char, 0) + 1

  max_freq = max(freq.values())
  candidates = [ch for ch, frequency in freq.items() if frequency == max_freq]

  return min(candidates)

print(norm_anal(s))

"""
* "One function one job" -> so can try to split the clean fuction
* after writing code -> see if you can squeeze the lines of code
"""