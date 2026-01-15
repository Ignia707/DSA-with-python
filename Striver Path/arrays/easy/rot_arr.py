arr = [1, 2, 4, 7, 7, 5, 3]  

"""
For Right Rotation by k steps:
- Reverse the entire array
- Reverse the first k elements
- Reverse the remaining n - k elements


For Left Rotation by k steps:
- Reverse the first k elements
- Reverse the remaining n - k elements
- Reverse the entire array

im doing here "right" btw
"""

rint("original: ", arr)
arr.reverse()
arr1, arr2 = arr[:2], arr[2:] # ! 2 is shift to right

print("reversed: ", arr)
print("before")
print(arr1)
print(arr2)

arr1.reverse()
arr2.reverse()

print("after")
print(arr1)
print(arr2)

arr = arr1 + arr2
print("rotated: ", arr)