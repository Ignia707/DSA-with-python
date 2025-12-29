N = 5

def print_rev_for(n, N):
    if n < 1:
        return
    
    print(n, end=" ")
    print_rev_for(n-1, N)

# * i got "4 3 2 1 5" initially
# 
def print_rev_back(n):
    if n < 1:
        return
    
    print_rev_back(n-1)
    print(n, end=" ")

print_rev_for(N, N)
# print_rev_back(N)