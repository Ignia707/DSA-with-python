from count_freq import count_num

arr = [10, 5, 10, 15, 10, 5]

def get_high_low(arr):
    freq_dict = count_num(arr)
    highest, lowest = arr[0], arr[0]

    for num, freq in freq_dict.items():
        if freq_dict[highest] < freq:
            highest = num
        if freq_dict[lowest] > freq:
            lowest = num
    
    return highest, lowest

def get_high_low_clear(arr):
    freq_dict = count_num(arr)

    highest = lowest = None
    max_freq = float('-inf')
    min_freq = float('inf')

    for num, freq in freq_dict.items():
        if freq > max_freq:
            highest = num
            max_freq = freq
        if freq < min_freq:
            lowest = num
            min_freq = freq

    return highest, lowest

print(get_high_low_clear(arr))