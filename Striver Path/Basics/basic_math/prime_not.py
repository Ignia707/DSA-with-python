N = [4554, 7789]

"""

divisors -> 1, itself

THE CURSED MATH'S IDEA:

math -> cursed

algorithm:
1. handle edges below and equal to 3
2. if divisible by 2, 3 then not prime
3. take i = 5 that is of form 6k - 1 (put k = 1)
4. iterate and check 6k - 1 and 6k + 1 is divisible -> if yes => Not prime

"""

import math

# * divisors finding logic
def prime_or_not(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

# ! math wizard way
def prime_or_not_math(n):
    if n <= 1:
        return False
    
    if n <= 3:
        return True
    
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5 # 6k - 1 (k = 1)
    while i * i <= n: # <= not < cause the middle divisor could be the turning point
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True

print(prime_or_not_math(3))