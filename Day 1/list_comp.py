nums = [[1,2],[3,4],[5,6]]

def generate_squares(upper):
  return [num ** 2 for num in range(1, upper + 1) if num % 2 == 0]

def flatten(matrix):
  return [cell for row in matrix for cell in row]

def odd_cubes(upper):
  return [num ** 3 for num in range(1, upper + 1) if num % 2 == 1]

print(generate_squares(20))
print("==================")
print(nums)
print("==================")
print(odd_cubes(15))