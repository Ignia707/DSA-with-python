"""
9 lines, 10 chars per line
index stars  d
  0     2    4
  1     4    3
  2     6    2
  3     8    1
  4     10   0
  5     8    1
  6     6    2
  
"""

# * i first complicated the value of stars as (10 - d) / 2 --> then ended up with this
# for i in range(9):
#   d = int(abs(4 - i))
#   spaces = 2 * d 
#   stars = 5 - d

#   print(f"{stars * "*"}{spaces * " "}{stars * "*"}")

# ! then generalized this pattern with mid, width
mid = 4 # the index of middle row
width = 5 # width of right half

# for i in range(2 * mid + 1):
#     stars = width - abs(mid - i)
#     spaces = 2 * abs(mid - i)
#     print("*" * stars + " " * spaces + "*" * stars)


"""
grey stars
7 lines, 4 chars per line

start, end --> all stars
odd index --> all spaces, even index --> middle all spaces

index stars spaces
  0     4     0
  1     0     4
  2     2     2
  3     0     4
  4     2     2
  5     0     4
  6     4     0

"""
# * i applied my ternery skill and single print() idea here
# height = 7
# width = 4

# for i in range(height):
#   stars = 2 if not (i % (height - 1)) else 0 if (i % 2) else 1
#   spaces = 4 - 2 * stars

#   if not (i % 2):
#     print(f"{stars * "*"}{spaces * " "}{stars * "*"}", end="")
#   print()

# ! here the idea is to make the flow cleaner, nothing else
# for i in range(height):
#   if (i == 0) or (i == (height - 1)):
#     print("*" * width)
#   elif (i % 2 == 0):
#     print("*" + " " * (width - 2) + "*")
#   else:
#     print()

"""
7 lines, 

index     nums    dist
  0     4 4 4 4     3 
  1     4 3 3 3     2
  2     4 3 2 2     1
  3     4 3 2 1     0
  4     4 3 2 2     1
  5     4 3 3 3     2
  6     4 4 4 4     3
"""

height = 7
center_ind = height // 2

# * initially i thot of distance from middle concept correctly, but can't relate it to the pattern
# ! then i got idea to take two distances then max(row_d, col_d) --> the "number" layer (outermost layer: 3)
# ? replaced "3" with `center_ind` 

"""
MAIN IDEA --> layer wise pattern finding
"""
for i in range(height):
  for j in range(height):
    print(f"{max(abs(center_ind - j), abs(center_ind - i)) + 1}", end=" ")
  print()