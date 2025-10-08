input= [1,2,3,4,5]

def not_Inplace(input):
  reversed = [input[i] for i in range(len(input) - 1, -1, -1)]
  print(reversed)

def Inplace(input):
  left, right = 0, len(input) - 1

  while (left < right):
    # safe to assign like this in python cuz of "tuple unpacking"
    # basically python evaluates the RHS first then assigns the value to LHS at the same time
    input[left], input[right] = input[right], input[left]
    left += 1
    right -= 1

  print(input)

Inplace(input)