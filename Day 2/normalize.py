input = " Hello      Python Learners "

def normalize (input):
  return " ".join(input.strip().lower().split())

print(input)
print(normalize(input))