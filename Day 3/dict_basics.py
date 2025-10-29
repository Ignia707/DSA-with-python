student = {
  "name": "Alice",
  "age": 20,
  "major": "CS",
}

print(student["name"])

student["age"] = 21
student["Grade"] = "A"

print("After update")
print(student)

print("Iterating.......")
for key, value in student.items():
  print(key, ":", value)

# ! my work from this point

marks = {
  "math": 90,
  "science": 86,
  "english": 87,
}

marks["opt"] = 74
marks["math"] = 100

for key, value in marks.items():
  print(f"{key}:{value}")

