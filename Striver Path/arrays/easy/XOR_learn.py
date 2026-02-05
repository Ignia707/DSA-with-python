"""

- a ⊕ a = 0

- a ⊕ 0 = a

- XOR is reversible
(a ⊕ b) ⊕ b = a


"""


"""
finding pattern for missing number:
n = 4,
missing XOR_of_all
    0       4
    1       5
    2       6
    3       7
    4       0

n % 4:
- 0 -> n
- 2 -> 3 + 4 * 
- 3 -> 
- 4 -> 

new attempt:
n = 4,
present (4 is missing):0^1^2^3
actual (i mean the whole): 0^1^2^3^4
"""

print(0^1^2^3^4)
print(0^1^2^3)