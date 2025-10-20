# import string

# input = "A man, a plan, a canal: Panama"

# def converter(input):
#   return "".join("".join(list(char for char in input.lower() if char not in string.punctuation)).split())

# if (converter(input)) == converter("".join(reversed(input))):
#   print("True")
# else:
#   print("False")

# The above is not the cleanest way
# =========================================================

def is_palindrom(input):
  clean = "".join(char.lower() for char in input if char.isalnum())
  return clean == clean[::-1] # reduce the "".join()'s and boolean condition into one

print(is_palindrom("A man, a plan, a canal: Panama"))