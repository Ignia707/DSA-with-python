from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, max_vol = 0, len(height) - 1, 0
        while (left < right):
            max_vol = max((right - left) * min(height[left], height[right]), max_vol)
            
            if (height[left] < height[right]):
              left += 1
            else:
              right -= 1
            
        return max_vol
    
# 👇 test it
if __name__ == "__main__":
    sol = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    print(sol.maxArea(height))
