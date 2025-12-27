N = 0

def count_dig_len(N):
    return len(str(N))

def count_dig_(N):
    count = 0
    while N > 0:
        count += 1
        # ! if u use "/" then it won't return int for each division, so the loop won't terminate as you wanted
        N = N // 10
        print(N)
    
    return count

# # print(count_dig_len(N))
# print(count_dig_(N))
import math 

# ? log10 from math gives the value to which 10 is to be raised to be equal to N. Here the when the N is positive number only this works. 
# ? it's O(1) in time and space
def count_dig_opt(N):
    print(N)
    return math.floor(math.log10(N)) + 1

print(count_dig_opt(math.pi))