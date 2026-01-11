
# * this shows quick sort implementation without slicing

arr = [10, 16, 8, 12, 15, 6, 3, 9, 5]

# ? the passing of low, high and getting new index of pivot from partition I thot btw, i was just unsure ;)
# ! the low, high here pretty much acts like the one inside partition --> just indirectly makes sure the passed partition isn't a single element
def quick_sort_B(arr, low = 0, high = len(arr) - 1):
    if low >= high:
        return
    
    p = partition(arr, low, high)

    quick_sort_B(arr, low, p - 1)
    quick_sort_B(arr, p + 1, high)

def partition(arr, low, high):
    pivot = arr[low]
    i, j = low + 1, high

    while True:
        while arr[i] <= pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1

        if i > j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    
    arr[low], arr[j] = arr[j], arr[low]
    return j

print(f"Unsorted: {arr}")
quick_sort_B(arr)
print(f"Sorted: {arr}")