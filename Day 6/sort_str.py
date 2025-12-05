arr1 = ["cat", "a", "apple", "bat"]
arr2 = ["dog", "ant", "bee", "zoo", "car"]
arr3 = ["hi", "banana", "x", "code", "art"]

inputs = [arr1, arr2, arr3]

for i in inputs:
  print(sorted(i, key=lambda x:(len(x), x)))
  print("===================================")