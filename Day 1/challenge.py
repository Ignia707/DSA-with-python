matrix = [[1,2,3],[4,5,6],[7,8,9]]

result = [cell for row in matrix for cell in row if cell % 3 != 0]
result.reverse()

print(result)