N = 36

"""

Input: N = 36
Output: [1, 2, 3, 4, 6, 9, 12, 18, 36]  


Property: for any non-negative integer n, if d is a divisor of n then n/d is also a divisor of n. This property is symmetric about the square root of N

36 -> 36, 12, 9, 6, 4, 2, 1
18 -> 18, 9, 6,  [4.2426]  3, 2, 1
22 -> 22, 11, [4.6904]  2, 1

"""
import math

def print_divisors(n):
    divisors = []
    # ! calm down bro seriously, the actual answers are from once stupid tryhard anyway :)
    for i in range(1, math.ceil(math.sqrt(n)) + 1):
        if (n % i == 0):
            divisors.append(i)

    return divisors + [n / d for d in divisors[-2::-1]]

def print_divisors_opt(n):
    divisors = []

    for i in range(1, math.isqrt(n) + 1):
        if n % i == 0:
            divisors.append(i)
            if n != n // i:
                divisors.append(n // i)

    return sorted(divisors) 

"""

Note about "//":

DataType:

- 5 // 2      # 2      (int) -> if both are int
- 5.0 // 2    # 2.0    (float) -> if either one is float

Value:

- (-5) // 2     # -3   (floors toward -∞)
- int(-5 / 2) # -2   (truncates toward 0)

"""

print(print_divisors_opt(N))