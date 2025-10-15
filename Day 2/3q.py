S = ["abc", "bca", "dbe"]

def solution(S):
  common_index = []
  n = len(S)

  for i in range(n):
    for j in range(i+1, n):
      a, b = S[i], S[j]
      common_letter = next(iter((set(a) & set(b))))

      for index, char in enumerate(a):
        if common_letter == char:
          common_index.append([i, j, index])
          break

  return common_index

print(solution(S))