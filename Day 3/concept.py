nums = {1: "one", 2: "two", 3: "three", 4:"four", 5:"five", 103:"drem"}

print(103 in nums)

if (103 in nums):
  print(nums.pop(103))

else: 
  nums[103] = "dremmmm"

print(nums)

# * collections.Counter

from collections import Counter

s = "banana"
count = Counter(s)
print(count)

print(count['a'])
print(count.most_common(2))
print(list(count.elements()))

# ! my work

prob = "mississippi"

def high_freq (input):
  return Counter(input).most_common(1)

print(high_freq(prob))

