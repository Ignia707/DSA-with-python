"""
Given two sorted arrays, arr1, and arr2 of size n and m. Find the union of two sorted arrays.
The union of two arrays can be defined as the common and distinct elements in the two arrays.

NOTE: Elements in the union should be in ascending order.
"""

arr1 = [1,2,3,4,5]
arr2 = [2,3,4,4,5]

def union(arr1, arr2):
    return list(set(arr1 + arr2))

def union_set(arr1, arr2):
    st = set(arr1) | set(arr2)
    
    return sorted(st)

def two_point_union(arr1, arr2):
    union = []

    while (arr1 and arr2):
        if arr1[0] < arr2[0]:
            if arr1[0] not in union:
                union.append(arr1[0])
                arr1.pop()
            arr1.pop()
        else:
            if arr2[0] not in union:
                union.append(arr2[0])
                arr2.pop()
            arr2.pop()
    
    print(union)
    if arr1:
        while arr1:
            if arr[0] not in union:
                union.append(arr[0])
                arr1.pop()
            arr1.pop()
    else:
        while arr2:
            if arr2[0] not in union:
                union.append(arr2[0])
                arr2.pop()
            arr2.pop()
    
    return union


# print(union_set(arr1, arr2))
print(two_point_union(arr1, arr2))