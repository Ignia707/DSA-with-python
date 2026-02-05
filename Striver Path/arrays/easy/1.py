arr = [1, 2, 4, 7, 7, 5, 3]  

# print(set(arr)) # ! to check set(arr) gives it sorted order, turns out it does :)
# print("original: ", arr)
arr.reverse()
arr1, arr2 = arr[:2], arr[2:]
# print(arr1)
# print(arr2)

# print("reversed: ", arr)
# print("before")
# print(arr1)
# print(arr2)

arr1.reverse()
arr2.reverse()

# print("after")
# print(arr1)
# print(arr2)

arr = arr1 + arr2
# print("rotated: ", arr)
print(int(2.9999999999999999999999999999999999999999999999999999999999999999999999999999))