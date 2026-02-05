"""
- the diff here is the array can include negative numbers
"""

"""
try1:
    - go element by element then verify curr_sum not < k  
    - inight: so in the while loop we assume that by each iteration we decrease curr_sum but if we are removing a negative number can increase currs_sum (so for a specific input it might fail)

try2:

"""

# * worked fr this lol :)
Array = [3, 4, -7, 1, 3, 3, 1, -4]
k = 7


def longestSubarrayWithSumKNeg1(arr, k):
    max_subarray_len = 0
    curr_sum = 0
    i = 0

    for j in range(len(arr)):
        curr_sum += arr[j]

        while curr_sum > k:
            curr_sum -= arr[i]
            i += 1

        if curr_sum == k:
            max_subarray_len = max(max_subarray_len, j - i + 1)
    return max_subarray_len

res = longestSubarrayWithSumKNeg2(Array, k)
print(res)