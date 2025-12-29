"""

Methods:

1. Brute force: traverse in reverse, place the elements in a new array
2. Two pointers: iterate till middle of array, swap two pointers array values every iteration
3. slicing in python. not in-place
    Time Complexity: O(n), because each element is visited once and possibly swapped once with its mirror index.
    Space Complexity: O(n) for slicing since it creates a new list and then assigns back (unless using two pointers).

"""

arr = [1, 2, 3, 4, 5]

def rev_arr_2pt(arr):
    length = len(arr)
    p1, p2 = 0, length - 1

    for _ in range(length // 2):
        arr[p1], arr[p2] = arr[p2], arr[p1]
        p1 += 1
        p2 -= 1
    
    return arr

# print(rev_arr_2pt(arr))

def rev_arr_slice(arr):
    return arr[::-1]

print(rev_arr_slice(arr))