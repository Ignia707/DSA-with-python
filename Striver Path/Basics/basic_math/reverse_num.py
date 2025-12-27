
# * pretty straightforward i believe
N = 10400

def reverse_num(N):
    reversed_num = 0
    
    # ! remember the time complexity here and count_digits is log10(N) because we N //= 10, so we kinda get the log10(N) total iterations if we change N like this. Theoretically if we N //= 5 then it's log5(N)
    while N > 0:
        reversed_num = reversed_num * 10 + (N % 10)
        print(N)
        N //= 10
        
    return reversed_num

print(f"\n{reverse_num(N)}")