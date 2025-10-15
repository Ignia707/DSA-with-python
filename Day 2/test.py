a = "abc"
b = "dbe"

c = (set(a) & set(b))

str_c = next(iter(c))
print(str_c)
print(str_c == "b")
print(a)