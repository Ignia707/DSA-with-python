"""

same logic as bubble_sort_recur, just the fact we need to pass the sorted array length

"""

arr = [13,46,24,52,20,9]

def insertion_sort_recur(arr, n=0):
    if n == len(arr):
        return arr
    
    curr = n   # ! to track the curr ind as we move through in left-partition and stop before the loop goes index-out-of bound to the left (like 0 and -1)
    while curr > 0 and arr[curr] < arr[curr - 1]: # ! also not `curr >= 0` cuz you are inherently doing what the above "!" statement lol
        arr[curr], arr[curr - 1] = arr[curr - 1], arr[curr]
        curr -= 1

    return insertion_sort_recur(arr, n + 1)


# * separating the loops by two functions
def insertion_sort_recur_clean(arr, n=1):
    if n == len(arr):
        return arr
    
    arr = insert(arr, n)

    return insertion_sort_recur_clean(arr, n + 1)

def insert(arr, n):
    if n == 0:
        return arr
    
    if arr[n - 1] > arr[n]:
        arr[n], arr[n - 1] = arr[n - 1], arr[n]
    
    return insert(arr, n - 1)

print(arr)
print(insertion_sort_recur_clean(arr))