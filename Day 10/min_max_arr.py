test1 = [3, 2, 1, 56, 10000, 167]
test2 = [-1, -5, -10, -2, 0]
test3 = [42]

def max_min(array):
    if len(array) == 1:
        return array[0], array[0]
    array.sort()

    min_val, *_, max_val = array
    return min_val, max_val

print(max_min(test3))