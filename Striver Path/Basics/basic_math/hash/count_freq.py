from collections import defaultdict, Counter

arr = [10,5,10,15,10,5]

def count_num(input_arr):
    hash_array = [0] * 16
    hash_map = {}
    counter_freq = Counter(arr)
    default_freq = defaultdict(int)

    for num in arr:
        hash_array[num] += 1
        hash_map[num] = hash_map.get(num, 0) + 1
        default_freq[num] += 1
    
    # print(hash_array)
    # print(hash_map)
    # print(counter_freq)
    # print(default_freq)
    return default_freq


count_num(arr)