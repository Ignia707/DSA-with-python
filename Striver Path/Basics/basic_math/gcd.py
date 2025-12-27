"""
Brute force:

- iterate
- find common factors
- update gcd as iteration goes on

"""

GCD = 1
N1 = 20
N2 = 15

def gcd_brute(n1, n2):
    for i in range(2, min(n1, n2) + 1):
        if (n1 % i == 0 and n2 % i == 0):
            GCD = i
    
    return GCD

# print(gcd_brute(N1, N2))



"""
Better approach:

same as brute force but iteration from min(N1, N2) till 1

"""

def gcd_better(N1, N2):
    # ! no need variable cause the first common divisor we find is GCD
    # GCD = 1

    for i in range(min(N1, N2), 1, -1):
        if (N1 % i == 0 and N2 % i == 0):
            return i
    
    return 1

# print(gcd_better(N1, N2))



"""
Optimal approach:

Euclidean Algorithm:

The Euclidean Algorithm is a method for finding the greatest common divisor (GCD)
of two numbers. It operates on the principle that the GCD of two numbers remains
the same even if the smaller number is subtracted from the larger number.

Kinda repeatedly subtract the current smaller number from the bigger until one of them is 0. The other is GCD ~ lol math :)

# ! EUCLIDEAN ALGO -----------
If a = bq + r (where r = a % b), then

gcd(a, b) = gcd(b, r) => when r = 0, the b is the GCD
# ! --------------------------

"""

# ! i was proud i wrote this clean code
def gcd_optimal(N1, N2):
    while N1 * N2 != 0:
        if (N1 > N2):
            N1 %= N2
        else:
            N2 %= N1
    
    return max(N1, N2)

# ! then GPT gave this ;-;
def gcd_more_clean(N1, N2):
    # ? the number in the loop conditional doesn't matter
    # * we just need to modify the tuple unpacking line according to the algorithm
    while N1 != 0:
        print(f"N1: {N1}", end=" ")
        print(f"N2: {N2}")

        N2, N1 = N1, N2 % N1
    
    return N2

print(gcd_more_clean(N1, N2))