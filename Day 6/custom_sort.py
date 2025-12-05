def custom_sort(arr):
  return sorted(arr, key=lambda x:(x%2 != 0, x))

arr1 = [5, 2, 8, 3, 1, 4]
arr2 = [7, 6, 9, 10, 12, 1]
arr3 = [11, 14, 2, 3, 9, 8, 16]

inputs = [arr1, arr2, arr3]

for i in inputs:
  print(custom_sort(i))