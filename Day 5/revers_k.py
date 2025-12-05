"""
Docstring for Day 5.revers_k
  Reverse first k elements of queue
"""

def reverseddd(q, k):
  if not q:
    return -69
  
  elif len(q) < k:
    return q
  
  else:
    revert = q[:k]
    return revert[::-1] + q[k:]

k = 3
test1 = []
test2 = [1,2]
test3 = [10, 20, 30, 40, 50]

print(reverseddd(test3, k))

"""
# ! also did the LC 20 today
"""