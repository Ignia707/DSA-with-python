# caeser cipher shift (lower-case only)

input = "xyz"

def css (input, key):
  return "".join(chr((ord(char) - 97 + key) % 26 + 97) for char in input if ord(char))

"""
============================
==== LOGIC OF THE SHIFT ====
============================
1. [x = ord(char) - 97] -> change to alphabetical index (0 - 25)
2. [y = x + key] -> new alphabetical index 
3. "% 26" keeps the value between (0 - 25) <== "%" returns the remainder
4. from the previous step, we got non-overflowing alphabetical index now we add it with "97" to get ASCII value
"""

print(css(input, 20))