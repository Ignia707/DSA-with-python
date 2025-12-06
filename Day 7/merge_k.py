import heapq

test = [
  [5, 10, 10, 20],
  [1, 1, 2, 50],
  [3, 9, 9, 30, 40],
  [0, 100]
]



# def merge_k(arr):
#   new_heap = [item for sub in arr for item in sub]
#   heapq.heapify(new_heap)

#   return heapq.nsmallest(len(new_heap), new_heap)

# print(merge_k(test))

def merge_k_opt(arr):
  heap, final = [], []

  for i in range(len(arr)):
    heapq.heappush(heap, (arr[i][0], i, 0))

  while heap:
    value, list_ind, value_ind = heapq.heappop(heap)

    final.append(value)

    next_ind = value_ind + 1
    if (next_ind < len(arr[list_ind])):
      heapq.heappush(heap, (arr[list_ind][next_ind], list_ind, next_ind))

  return final

print(merge_k_opt(test))