"""

? IDEA: keep splitting the array into halves until the split parts are single elements. use merge() between them to get the sorted order of the merging elements --> REPEAT

? Merge: So it compares first elements from each array --> appends in new array while removing the smaller one out --> repeat until exhaustion ==> append the rest of the other array

Eg:
Left  = [2, 5, 8]
Right = [3, 6, 7]

Compare 2 and 3 → take 2
Result = [2]

Compare 5 and 3 → take 3
Result = [2, 3]

Compare 5 and 6 → take 5
Result = [2, 3, 5]

Compare 8 and 6 → take 6
Result = [2, 3, 5, 6]

Compare 8 and 7 → take 7
Result = [2, 3, 5, 6, 7]

Right is empty → append rest of Left
Result = [2, 3, 5, 6, 7, 8]


"""

input_arr = [3,2,8,5,1,4,23]

def merge(a, b):
    c = []

    while (a and b):
        if (a[0] > b[0]):
            c.append(b[0])
            b.pop(0)
        else:
            c.append(a[0])
            a.pop(0)
    
    if not a:
        c += b
    else:
        c += a
    
    return c

def merge_sort(arr):
    half = len(arr) // 2

    if not half:
        return arr

    left = merge_sort(arr[:half]) # ! i made a infinite recur error here, explained below
    right = merge_sort(arr[half:])

    return merge(left, right)


"""

when we split like `left has all elements till middle element` and right has rest. issue occurs with len(arr) = 2
that is,

!left  = arr[:half + 1]
!right = arr[half + 1:]

arr = [a, b]
len(arr) = 2
half = 1

left  = arr[:2]  → [a, b]   (same array again!)
right = arr[2:]  → []

so remember,
? Left part -→ indices before mid. Right part -→ indices from mid onward

"""

print(input_arr)
print(merge_sort(input_arr))