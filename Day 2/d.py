s = "A man, a plan, a canal: Panama"

def clean (input):
  return ("".join([char.lower() for char in input if char.isalpha()])).strip()

def ispal (input):
  return (input == input[::-1])

print(clean(s))
print(ispal(clean(s)))