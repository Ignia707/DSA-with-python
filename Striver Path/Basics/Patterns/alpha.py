"""
5 lines
index count
  0     5
  1     4
  2     3
  
  4     1

start with "A"
count = 5 - index
"""

# for i in range(5):
#     for j in range(5 - i):
#         print(f"{chr(65 + j)} ",end=" ")
#     print()

"""
5 lines
same as above (the one before the above i meant) for index, count

EACH LINE --> ONE LETTER
"""

# for i in range(5):
#     for _ in range(i + 1):
#         print(f"{chr(65 + i)} ", end=" ")
#     print()


"""
triangle ABA 
4 lines, 7 chars total per line (include spaces)
symmetry at center

index count 
  0     1
  1     3
  2     5
  3     7

count = 2 * index + 1
"""
# * i first tried to make this by left and right halves ==> two loops
# ! tried to reduce it to one loop ==> over complicated the "else" j value
# ? need to try combinations with indices first  

# for i in range(4):
#     left_space = 3 - i
#     letters = ""

#     for j in range(2*i + 1):
#         offset = j if j <= i else 2*i - j
#         letters += chr(65 + offset)

#     print(f"{left_space * " "}{letters}{(left_space - 1) * " "}")


"""
E, DE question. right angle triangle
5 lines
count = index + 1
"""

# for i in range(5):
#     for j in range(i + 1):
#         print(chr((69 - i) + j), end=" ")
#     print()


""" 
rectangle of stars with diamond space
10 lines
10 chars per line (with spaces)

index space
  0     0
  1     2
  2     4
  3     6
  4     8

space = 2 * index
"""

# * first i tried to have separate formulae for stars, space for i < 5 and other
# ! then i created a variable "d" that is the distance from nearest edge to use it for stars, space single formulae - each

for i in range(10):
    d = i if i < 5 else 9 - i
    stars = (5 - d)  * "*"
    space = (2 * d) * " "

    print(f"{stars}{space}{stars}",end="")
    print()