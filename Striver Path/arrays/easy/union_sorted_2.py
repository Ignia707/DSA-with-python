"""
IDEA:

- add smaller ones to new array, move smaller pointer
- if equal add once --> move both pointers
! Don't pop() like in merge sort

! Infinite loops -> check pointer increment / decrement

"""

# arr1 = [1,2,3,4,5]
# arr2 = [2,3,4,4,5]

arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [2, 3, 4, 4, 5, 11, 12]

# ! this code misses the part where the remaining elements of the longer array needs to be added
def two_point_union(arr1, arr2):
    union = []
    i, j = [0] * 2

    while (i < len(arr1)) and (j < len(arr2)):
        if arr1[i] < arr2[j]:
            if not check_duplicate(union, arr1[i]):
                union.append(arr1[i])
            i += 1
                
        
        elif arr1[i] > arr2[j]:
            if not check_duplicate(union, arr2[j]):
                union.append(arr2[j])
            j += 1
        
        else:
            if not check_duplicate(union, arr1[i]):
                union.append(arr1[i])
            j += 1
            i += 1

    return union

def check_duplicate(arr, num):
    return num in arr

result = two_point_union(arr1, arr2)
# print(result)

"""
Optimize steps:

- Removing check_duplicate (it’s an O(n) lookup every time).

- Using the sorted property of the arrays.

- Tracking only the last inserted element to avoid duplicates.

- Appending remaining elements after the main loop.

"""

def union_opt(arr1, arr2):
    union = []
    i, j = [0] * 2

    while (i < len(arr1)) and (j < len(arr2)):
        if arr1[i] < arr2[j]:
            val = arr1[i]
            i += 1
                
        
        elif arr1[i] > arr2[j]:
            val = arr2[j]
            j += 1
        
        else:
            val = arr1[i]
            j += 1
            i += 1
        
        # * separate appending from other processes
        if not union or union[-1] != val:
            union.append(val)

    while i < len(arr1):
        if arr1[i] not in union:
            union.append(arr1[i])
        i += 1 
    
    while j < len(arr2):
        if arr2[j] not in union:
            union.append(arr2[j]) 
        j += 1

    return union

print(union_opt(arr1, arr2))