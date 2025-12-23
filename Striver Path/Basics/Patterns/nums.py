# """
# start num 1 if index == even else 0
# 5 lines
# """

# # * Progress
# # ! First change ---> removed if for checking 1 or not
# # ? directly got element from the value of i

# for i in range(5):
#     val = (i + 1) % 2

#     for _ in range(i + 1):
#         print(f"{val} ", end="")
#         val = 1 - val
#     print("\n")

"""
4 lines
1... 12... 123... 1234 ==> space then reverse

space   4 -> 2 -> 1 -> 0
letters 2 -> 4 -> 6 -> 8
index   0 -> 1 -> 2 -> 3

total chars = 8
letters -> 2 * (i + 1)
space -> 8 - letters

===========

index numbers
  0     1
  1     1 2 
  2     1 2 3
  3     1 2 3 4
"""     
# * initially thought of using space based approach
# ! then GPT fked me over some space related retarded login --> but gave me insight to join left and right
# ? then i finally fixed the whole by: indices in left (+2) and the space logic the same 

# for i in range(4):
#     left = "".join(str(x) for x in range(1, i+2))
#     right = "".join(str(x) for x in range(i+1, 0, -1))

#     print(f"{left}{" " * (8 - 2 * len(left))}{right}")


"""
5 lines
index   start  count  nums
0         1     1     1
1         2     2     2 3
2         4         
3         7
4         11

count = index + 1
"""

# * the first one below is quite obvious iterate with count and have a value to keep track of count
# ! the second method is finding the start value of each line -> use that as value
# ? i thot of summing all rows before getting that value, but lol it's actually sum of elements in range(i), i being the current row's index

# val = 1
# for i in range(5):
#     for j in range(i + 1):
#         print(val, end=" ")
#         val += 1
#     print("\n")

# for i in range(5):
#     start = 1 + sum(j + 1 for j in range(i))
    
#     for _ in range(i + 1):
#         print(start, end=" ")
#         start += 1
#     print("\n")    

"""
5 lines, start with "A"
pretty straight forward, the second is just more `pythonic`
"""

# for i in range(5):
#     val = 65
#     for _ in range(i + 1):
#         print(chr(val), end=" ")
#         val += 1
#     print("\n")

# for i in range(5):
#     for j in range(i + 1):
#         print(f"{chr(j + 65)}", end=" ")
#     print()

