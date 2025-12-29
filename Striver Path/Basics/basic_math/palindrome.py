N1 = 12321
N2 = 7789

def reverse_num(N):
    reversed_num = 0
    
    # ! remember the time complexity here and count_digits is log10(N) because we N //= 10, so we kinda get the log10(N) total iterations if we change N like this. Theoretically if we N //= 5 then it's log5(N)
    while N > 0:
        reversed_num = reversed_num * 10 + (N % 10)
        N //= 10
        
    return reversed_num

def palindrome(n):
    return n == reverse_num(n)

"""
The idea is simple if 12321 is the number, then checking the first half is sufficient
That is, if it's palindrome then the same sequence would be in 2nd half

Edge cases -> less than zero, multiple of 10

while exiting while loop,
for 12321,
Odd number of digits -> rev = 123, n = 12 ==> (rev // 10) to take the middle element out

for 1221, 
Even number of digits -> rev = 12, x 12
"""

def palindrome_optimized(n):
    if (n < 0) or (n % 10 == 0 and n > 0):
        return False
    
    rev = 0
    while (n > rev):
        # ! be careful here, it's not ADDING it's re-assigning
        rev = (rev * 10) + (n % 10)
        n //= 10
    
    return n == rev or n == (rev // 10)

# print(int(palindrome(N1)))
print(palindrome_optimized(N1))