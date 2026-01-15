"""

Problem Statement: Given an array, find the second smallest and second largest element in the array. Print ‘-1’ in the event that either of them doesn’t exist.

"""

arr1 = [1, 2, 4, 7, 7, 5]  
arr2 = [1, 2, 1]

# * idea to get sec_large, sec_small from largest, smallest - doesn't satisy [1, 1, 1]
def second_large_small(arr):
    if len(arr) <= 2:
        return -1

    [largest, smallest] = [arr[0]] * 2 # ! this is the correct notation
    [sec_largest, sec_smallest] = [float('-inf'), float('inf')]

    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
        if arr[i] < smallest:
            smallest = arr[i]
        
    for i in range(len(arr)):
        if arr[i] > sec_largest and arr[i] != largest:
            sec_largest = arr[i]

        if arr[i] < sec_smallest and arr[i] != smallest:
            sec_smallest = arr[i]
    
    if sec_largest == largest:
        sec_largest = -1
    if sec_smallest == smallest:
        sec_smallest = -1

    return sec_smallest, sec_largest

def second_large_small_opt(arr):
    if len(arr) <= 2 or len(set(arr)) < 3:
        return (-1, -1)

    small, second_small = [float('inf')] * 2
    large, second_large = [float('-inf')] * 2

    for num in arr:
        if num > large:
            second_large, large = large, num
        elif num > second_large and num != large: # ! the second conditional to handle duplicate
            second_large = num

        if num < small:
            second_small, small = small, num
        elif num < second_small and num != small:
            second_small =  num
    
    return second_large, second_small


# * with helper function
def second_large_small_cleanest(arr):
    if len(set(arr)) < 3: # ! convers both length and duplicates when len() == 3
        return (-1, -1)
    
    return second_extreme(arr, True), second_extreme(arr, False)

def second_extreme(arr, findMax = True):
    first = float('-inf') if findMax else float('inf')
    second = first

    for num in arr:
        if (findMax and num > first) or (not findMax and num < first):
            first, second = num, first
        elif (num != first) and (
            (findMax and num > second) or
            (not findMax and num < second)):
            second = num

    return second

print(second_large_small_cleanest(arr1))