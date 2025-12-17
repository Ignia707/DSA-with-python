arr = [1, 2, 3, 4, 5]

def sum_arr(array, index=0):
    if index == len(array):
        return 0

    return array[index] + sum_arr(array, index + 1)

print(sum_arr(arr))