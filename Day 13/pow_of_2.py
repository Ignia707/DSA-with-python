n = 18

# ! brute force
def pow_of_2(num):
    i = 0
    while i < num:
        if (1 << i == num):
            return True
        i += 1
    
    return False

# * the bit-wise way

def pow_of_2_bit(num):
    return num > 0 and not (num & (num - 1))

"""
binary of n (2 pow number) --> only 1 bit = 1, rest = 0
biary of n -1 --> all bits right of the "1" bit is 1 and 0 in "1" bit position

4 = 0100
3 = 0011

"""

print(pow_of_2(n))