"""
4 lines, 7 chars total per line (include spaces)
symmetry at center

index count 
  0     1
  1     3
  2     5
  3     7

count = 2 * index + 1
"""

for i in range(4):
    left_space = 3 - i
    letters = ""

    for j in range(2*i + 1):
        offset = j if j <= i else 2*i - j
        letters += chr(65 + offset)

    print(f"{left_space * " "}{letters}{(left_space - 1) * " "}")