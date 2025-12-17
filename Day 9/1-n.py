def one_n(n):
    if n == 1:
        return print(n)
    
    one_n(n-1)
    print(n)

one_n(19)