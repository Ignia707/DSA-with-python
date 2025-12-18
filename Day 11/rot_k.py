nums = [1, 2, 3, 4, 5, 6, 7]
k = 23

def rot_arr(arr, k):
    k %= len(arr)
    return arr[-k:] + arr[:-k]

print(rot_arr(nums, k))