n = -1

def count_set_bits(num):
    count = 0
    while num:
        num = num & (num - 1)
        count += 1

    return count

def count_set_bits_neg(num):
    num &= 0xFFFFFFFF
    count = 0
    while num:
        num &= num - 1
        count += 1

    return count

print(count_set_bits_neg (n))