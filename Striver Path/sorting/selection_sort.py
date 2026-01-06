"""

Idea: Two partitions (sorted, unsorted - same array) Iterate over unsorted to get min element -> append it in sorted

Params:
- curr min
- curr element
- partition end


"""

arr = [13,46,24,52,20,9]

def selection_sort(input_arr):
    length = len(input_arr)
    curr_min = float('inf')
    min_ele_ind = None

    for i in range (length - 1): # ! "i" is the start of the unsorted partition
        curr_min = input_arr[i]

        for j in range(i + 1, length):
            if curr_min > input_arr[j]:
                curr_min = input_arr[j]
                min_ele_ind = j
    
        input_arr[i], input_arr[min_ele_ind] = curr_min, input_arr[i]

    return input_arr

# * removed the curr_min and added conditional to swap
def selection_sort_clean(input_arr):
    length = len(input_arr)
    min_ele_ind = None

    for i in range(length - 1):
        min_ele_ind = i

        for j in range(i + 1, length):
            if input_arr[min_ele_ind] > input_arr[j]:
                min_ele_ind = j
        
        if min_ele_ind != i: # ! if it's not equal to "i" it is swapped. See above 2nd loop
            input_arr[i], input_arr[min_ele_ind] = input_arr[min_ele_ind], input_arr[i]

    return input_arr

print(selection_sort_clean(arr))
# selection_sort(arr)