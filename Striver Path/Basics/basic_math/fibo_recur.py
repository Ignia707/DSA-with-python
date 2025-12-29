"""

Given an integer N. Print the Fibonacci series up to the Nth term
NOTE: # ! start from 0 

Fib(N) = Fib(N - 1) + Fib(N - 2) # ! don't use this format
fN = fN-1 + fN-2 # ? use this, the point is "N" is not the value but index of the fib series 
with f0 = 0, f1 = 1 

"""

# ! let this be in the hall of f(sh)ame codes, lol ;-;
def fib_recur(n):
    if n == 0 or n == 1:
        return n

    return n + fib_recur(n - 1) + fib_recur(n - 2)

# print(fib_recur(7))


def better_fib_iter(n):
    if n == 0:
        print(n)
        return 1

    second_last = 0
    last = 1

    print(f"{second_last} {last}", end=" ")

    for i in range(2, n):
        print(second_last + last, end=" ")

        # ! here use temp so that one of info is not lost else use this
        last, second_last = second_last + last, last

# better_fib_iter(0)

# * proper recursion -> with this kinda of recursion i can't get the series
"""

the idea to print "last" every iteration is correct, but that applies in the last case of implementation. here you need to pass it in the function to get the correct series.

# ? WHY: Every recursive call forgets previous values

"""
def opt_fib(n): # gives the nth element in the fibnaaci
    if n <= 1:
        return n
    
    last = opt_fib(n - 1)
    second_last = opt_fib(n - 2)
    
    return last + second_last

# print(opt_fib(4)) 

def opt_fib_series(n, curr=0, next=1): # gives the series itself
    if n == 0:
        return n
    
    print(curr, end=" ")
    return opt_fib_series(n - 1, next, curr + next)

# opt_fib_series(5)