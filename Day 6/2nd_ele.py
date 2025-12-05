arr1 = [(3, 10), (1, 5), (4, 7)]
arr2 = [(2, 9), (8, 3), (6, 12)]
arr3 = [(5, -1), (7, 4), (2, 0), (1, -5)]

inputs = [arr1, arr2, arr3]

for i in inputs:
  print(sorted(i, key=lambda x: -x[1]))
  print("==========================")

"""
skipped the start time thingy, it's the same 
"""