matrix = [[1,2,3],[4,5,6],[7,8,9]]

flat = [cell ** 2 for row in matrix for cell in row if cell % 2 == 1]
print(flat)