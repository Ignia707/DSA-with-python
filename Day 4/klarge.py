def findKthLargest(nums, k):
    unique = sorted(list(set(nums)))

    return unique[-k]

print(findKthLargest([3,2,3,1,2,4,5,5,6], 4))