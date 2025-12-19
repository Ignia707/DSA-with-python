a = -4
b = 9

def swap_XOR(a, b):
    return [a ^ a ^ b, b ^ b ^ a]

print(swap_XOR(a, b))