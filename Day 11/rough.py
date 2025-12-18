import copy

a = [[1, 2], [3, 4]]m

# * deepcopy
b = copy.deepcopy(a)
b[0][0] = 99

# * shallow copy
b = a[:]

print("a:", a)
print("b:", b)