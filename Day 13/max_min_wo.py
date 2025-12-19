nums = [-7, -3, -10, -2]

def max_min_wo(arr):
    min, max = arr[0], arr[0]

    for num in arr[1:]:
        if num < min:
            min = num
        if num > max:
            max = num
    
    return [max, min]

print(max_min_wo(nums)) 