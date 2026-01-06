"""

Hashing --> prestoring + fetching

Approaches:

1. Brute: iterate as you increment count
2. Hash Array: separate array for hash. The records are like hash_array[num] = freq_of_num

! QUICK TIP: 10⁸ operations take ~1 second

"""

arr = list(map(int, input("Enter numbers with spaces: ").split()))
"""
"""

# * hash array method 
# ! only limitted numbers hashable 
def hash_array():
    hash_array = [0] * 13
    for num in arr:
        hash_array[num] += 1
    print(hash_array)

    q = int(input("Enter number of queries: "))
    for _ in range(q):
        n = int(input("Enter number to check freq: "))
        print(f"Freq of {n}: ", hash_array[n])

    return 1

    