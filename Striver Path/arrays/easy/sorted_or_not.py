"""

Problem Statement: Given an array of size n, write a program to check if the given array is sorted in (ascending / Increasing / Non-decreasing) order or not. If the array is sorted then return True, Else return False.

"""

arr1 = [1,2,3,4,5]
arr2 = [1, 3, 2, 4, 5]
arr3 = [1]

def sorted_not(arr):
    length = len(arr)
    if length == 1:
        return True

    for i in range(1, length):
        if arr[i] < arr[i - 1]:
            return False

    return True

def is_sorted(arr):
    return all(arr[i] >= arr[i - 1] for i in range(1, len(arr)))
    # ! not all(arr[i] >= arr[i - 1]) for i in range(1, len(arr))

print(sorted_not(arr2))