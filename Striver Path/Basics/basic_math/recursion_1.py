name = "Ramana"
N = 5


def print_n(name, n):
    if n == 0:
        return 
    
    print(name)
    return print_n(name, n-1)

# * increment option - count, N separate variables
def print_n_inc(name, n, N):
    if n == N:
        return
    
    print(name)
    return print_n_inc(name, n + 1)

# print_n(name, N)
print_n_inc(name, 0, N)