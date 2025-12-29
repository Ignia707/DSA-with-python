N = 5

def _N_foward(n, N):
    if n > N:
        return 
    
    print(n, end=" ")

    return _N_foward(n + 1, N)

# * go deep into base case --> print while coming back
def _N_backtrack(n, N):
    if n > N:
        return
    
    _N_backtrack(n + 1, N)
    print(n, end=" ")

# _N_foward(1, N)
_N_backtrack(1, N)