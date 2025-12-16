arr1 = [1, 2, 3, 4]
arr2 = [9, 8]


for val1, val2 in zip(arr1, arr2, strict=True):
    print(val1, val2)