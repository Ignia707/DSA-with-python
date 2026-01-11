
# * ngl this by this method the code looks clean as fk but MEMORY IS EXTRA !!!

arr = [10, 16, 8, 12, 15, 6, 3, 9, 5]

def quick_sort_A(arr):
    if len(arr) <= 1:
        return arr

    left, pivot, right = partition(arr)

    return quick_sort_A(left) + [pivot] + quick_sort_A(right) # ! here if you give just "pivot" then "int can't be cancat with list" kinda error hits you

def partition(arr):
    pivot = arr[0]
    left, right = [], []

    for x in arr[1:]: # ! by this you are just making sure the pivot gets the right position. You don't care about the positions of elements inside left or right
        if x <= pivot:
            left.append(x)
        
        if x > pivot:
            right.append(x)

    return left, pivot, right

print(arr)
print(quick_sort_A(arr))