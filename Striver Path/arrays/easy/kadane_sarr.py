def maxSubArray(nums: List[int]) -> int:
        ansStart, ansEnd = 0, 0
        curr = best = nums[0]

        for i in range(len(nums)):
            if curr < 0:
                ansStart = ansEnd = i
                curr = nums[i]
            
            else:
                ansEnd += 1
                curr += nums[i]

            best = max(best, curr)
        
        return [best, nums[ansStart:ansEnd]]

nums = [5,4,-1,7,8]
res = maxSubArray(nums)
print(res[1])