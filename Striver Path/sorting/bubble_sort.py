"""

kinda opposite of selection sort: in each iteration we "bubble" the largest element to the right and left-append it to the "sorted partition"

params:
- curr (curr + 1 for next) --> "j" is enough

"""

arr = [13,46,24,52,20,9]

def bubble_sort(arr): # ? here we mutate the array we can use it as in-place changing function, look below function
    length = len(arr)

    for i in range(length):
        swapped = False

        for j in range(length - i - 1): # ! see in terms of number os comparisons. if "- 1" not there then for the last element this accesses "j + 1" which doesn't exist
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if swapped: # ? early break to avoid iteration if already swapped
            break

##### USAGE #####
print(f"Unsorted: {arr}")
bubble_sort(arr)
print(f"Sorted: {arr}")