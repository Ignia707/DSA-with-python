"""
was away for while, forgot stuffs :(
"""

# input = "  Hello Python Learners   "

# def normalize (input):
#   return input.strip().lower()

# print(normalize(input))

input = "A man, a plan, a canal: Panama"

def is_palindrome (input):
  clean = "".join(char.lower() for char in input if char.isalnum())
  return clean == clean[::-1]

print(is_palindrome(input))