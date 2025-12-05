students = [
    ("Ram", 85, 19),
    ("Kiran", 92, 18),
    ("Asha", 92, 20),
    ("Meena", 75, 18)
]

new_studs = sorted(students, key= lambda x: (-x[1], x[2], x[0]))
print(new_studs )  