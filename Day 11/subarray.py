nums = [2, 4, 6, 8]
target = 5

# ! below is brute fking force solution btw :")
# def subarray_sum(arr, target):
#     curr = start = 0
#     curr_sum = arr[start]

#     for _ in range(len(arr)-1):
#         for _ in range(curr + 1, len(arr)):
#             if(curr_sum == target):
#                 return True
#             elif (curr_sum > target):
#                 break

#             curr += 1
#             curr_sum += arr[curr]
        
#         start += 1
#         curr = start
#         curr_sum = arr[start]
    
#     return False

def subarray_slide_window(arr, k):
    left, curr_sum = 0, 0

    for right in range(len(arr)):
        curr_sum += arr[right]

        # * we don't need a left, right comparison
        while curr_sum > target:
            left += 1
            curr_sum -= arr[left]

        if curr_sum == target:
            return True

    return False    

print(subarray_slide_window(nums, target))