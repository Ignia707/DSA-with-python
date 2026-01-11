
# ! the below is my valiant attempt to implement quick sort and fumbled. I have 2 sep file with and w/o slicing. Enjoy :)

arr = [10, 16, 8, 12, 15, 6, 3, 9, 5]

def quick_sort(arr, low = 0, high = len(arr) - 1):
    if len(arr) <= 1:
        return arr
    
    partition(arr, low, high)

    arr[:new_high] = quick_sort(arr[:new_high])
    arr[new_high + 1:] = quick_sort(arr[new_high + 1:])

    return arr
    

def partition(arr, low, high):
    i, j = 1, len(arr) - 1
    pivot = arr[0]

    while True:
        while arr[i] <= pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1

        if i > j: # ! if the condition is added to the while in beginning, as the j and i values changes (i > j) can't be verified in the same loop
            break

        arr[i], arr[j] = arr[j], arr[i]

    arr[0], arr[j] = arr[j], arr[0]
    
    return arr

# print(f"Unsorted: {arr}")
quick_sort(arr)
# print(f"Sorted: {arr}")