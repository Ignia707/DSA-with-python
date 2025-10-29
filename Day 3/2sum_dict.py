"""
Question:
 
Given a list of numbers and a target sum, find two numbers that add up to the target.
Return their indices.
"""

nums = [2, 7, 2, 11, 15]
target = 4

def func (nums, target):
  num_indices = {}
  
  for i in range (len(nums)):
    complement = target - nums[i]

    if complement in  num_indices:
      return [i, num_indices[complement]]
    
    # * if you record the index before the "if" block then it'll take the index of itself twice
    num_indices[nums[i]] = i
    
  
  return -1
      
print(func(nums, target))


"""
1. check if the complement exist in dict
2. if yes -> return the indices
3. if no -> just append the number with index
"""