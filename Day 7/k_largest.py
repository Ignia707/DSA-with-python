import heapq

inputs = [
  [[7, 2, 5, 3, 9], 2],
  [[10, 4, 6, 20, 1], 3],
  [[50, 30, 40, 10, 20, 60], 4]
]

# def k_largest(arr, k):
#   heapq.heapify(arr)

#   return heapq.nlargest(k, arr)[-1] 

# for i, k in inputs:
#   print(k_largest(i, k))
#   print("======================")

def k_largest_opt(arr, k):
  heapq.heapify(arr)

  while (len(arr) > k):
    heapq.heappop(arr)
  return heapq.heappop(arr)

for i, k in inputs:
  print(k_largest_opt(i, k))
  print("======================")