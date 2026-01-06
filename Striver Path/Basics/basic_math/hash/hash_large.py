"""

Problem: Cannot hash numbers like 10⁹ or higher because we can't declare arrays that
large # ! Solution: dictionary (hashmap)

Key Advantage: Dictionary only stores elements that actually exist in the array,
unlike arrays which allocate space for all indices up to the maximum element. ~ obvious ik :)

"""

n = input("Enter numbers with spaces: ")
arr = list(map(int, n.split()))

# * classic dict
def count_num(arr):
    freq_dict = {}

    for num in arr:
        freq_dict[num] = freq_dict.get(num, 0) + 1
        # ! not same as "freq_dict[char] += freq_dict.get(char, 1)" --> when the key error arises
        
    # print(freq_dict)

# * using defaultdict
from collections import defaultdict

def count_num_default(arr):
    freq_dict = defaultdict(int)

    for num in arr:
        freq_dict[num] += 1
    
    print(dict(freq_dict))

count_num(arr)
count_num_default(arr)