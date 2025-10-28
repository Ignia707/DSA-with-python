# student = {"name": "Alice", "age": 20}

# print(student.get("name"))
# print(student.get("grade", "N/A"))

# print(student.setdefault("grade", "A"))
# print(student)

# # ! my work from here

# inventory = {"apple": 10, "banana": 5}

# print("orange:",inventory.get("orange", 0))
# print("orange:",inventory.setdefault("orange", 7))

# student = {"name": "Bob", "age": 22, "grade": "B"}

# for key, value in student.items():
#   print(f"{key}: {value}")

# print("=======================")

# for key in student.keys():
#   print(f"{key}")

# print("=======================")


# for value in student.values():
#   print(f"{value}")

# * Sets - {}, add(), remove(), discard()

# fruits = {"apple", "banana", "mango"}

# # print(fruits)
# # fruits.add("cherry")
# # fruits.add("apple")
# # print(fruits)

# print(fruits)
# fruits.remove("banana") # ! throws error if not found
# fruits.discard("orange") # ! handles if not found
# print(fruits)

# # ! my work 

# nums = {1, 2, 3}

# print(nums)
# nums.add(3)
# nums.remove(2)
# nums.discard(5)
# print(nums)

# * Set Operations — union (|), intersection (&), difference (-)

a = {10, 20, 30, 40} 
b = {30, 40, 50, 60}

print(a | b)
print(a & b)
print(a - b)