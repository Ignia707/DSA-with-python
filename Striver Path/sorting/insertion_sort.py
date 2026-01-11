"""

Idea: partition yes. Each element is compared with left element till it's in sorted position

Params:
- curr --> to track position as we move in left-partition
"""

arr = [13,46,24,52,20,9]

# * a lil (lot) confusing ik
def insertion_sort(arr):
    for i in range(1, len(arr)):
        left = i - 1

        while (left + 1) and arr[left + 1] < arr[left]:
            arr[left + 1], arr[left] = arr[left], arr[left + 1]
            left -= 1

def insertion_sort_clean(arr):
    for i in range(1, len(arr)):
        curr = i # ? used curr instead of left

        while (curr - 1) >= 0 and arr[curr] < arr[curr - 1]: # ? used >= instead of (simply (curr - 1) -> clarity)
            arr[curr], arr[curr - 1] = arr[curr - 1], arr[curr]
            curr -= 1

    
print(f"Unsorted: {arr}")
insertion_sort_clean(arr)
print(f"Sorted: {arr}")