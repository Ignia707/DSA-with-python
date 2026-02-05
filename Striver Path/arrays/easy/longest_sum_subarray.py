"""
this is for 
"""

def longestSubarrayWithSumK(a: [int], k: int) -> int:
    max_subarray_len = 0
    i, j = [0] * 2
    curr_sum = a[i]

    while j < len(a) - 1:
        # print(f"length: {max_subarray_len}")
        if curr_sum < k:
            # print(1)
            j += 1
            curr_sum += a[j]
        
        elif curr_sum > k:
            # print(2)
            curr_sum -= a[i]
            i += 1
        
        else:
            # print(3)
            max_subarray_len = max(max_subarray_len, j - i + 1)
            j += 1
            curr_sum += a[j]

    return max_subarray_len

# * clean 
def longestSubarrayWithSumK_clean(a: [int], k: int) -> int:
    i, curr_sum, max_length = [0] * 3

    """
    we are iterating the j with for, having while loop in the inside. So we are handling curr_sum < k condition implicitly
    here for every increment in j, while modifies curr_sum to == or < k, with i
    """
    for j in range(len(a)):
        curr_sum += a[j]
        while curr_sum > k:
            curr_sum -= a[i]
            i += 1
        
        if curr_sum == k:
            max_length = max(max_length, j - i + 1)
    
    return max_length

arr = [10, 5, 2, 7, 1, 9]
k = 15
print(longestSubarrayWithSumK_clean(arr, k))