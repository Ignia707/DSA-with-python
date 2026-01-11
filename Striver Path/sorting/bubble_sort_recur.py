"""

You replace two loops with recursions. but just replacing the outer one is simpler

n --> len of unsorted partition
"""

arr = [13,46,24,52,20,9]

def bubble_sort_recur(arr, n=len(arr)):
    if n == 1:
        return arr

    for i in range(n - 1): # ! again the if n was there then, it means n comparisons so the loops continues to compare till n-1 and n indices. but there are only n-1 indices
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    return bubble_sort_recur(arr, n - 1)

print(arr)
print(bubble_sort_recur(arr))