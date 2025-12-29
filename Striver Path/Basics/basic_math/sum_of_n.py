N = 5

"""

SUM of N numbers = [N * (N + 1) / 2 ]

Recursive approach: sum(N) = N + sum(N - 1)

"""

def sum_of_n(N):
    if N == 1:
        return N

    return N + sum_of_n(N - 1)

print(sum_of_n(N))