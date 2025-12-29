"""

Factorial of a number x: x! --> x * (x - 1) * (x - 2)..... * 1

"""

N = 5

def fact_recur(n):
    if n == 1:
        return 1
    
    return n * fact_recur(n - 1)

print(fact_recur(N))