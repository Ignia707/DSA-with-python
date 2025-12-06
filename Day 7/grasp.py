
import heapq

# arr = [12, 3, 7, 4, 9, 1]

# heapq.heapify(arr)

# heapq.heappop(arr)
# heapq.heappop(arr)

# heapq.heappush(arr, 5)

# print(arr)

arr = [5, 1, 8, 3]

# * apprach 1 to get max-heap

# max_heap = [-x for x in arr]
# heapq.heapify(max_heap)

# # ! pushed 6 but stored as "-6"
# heapq.heappush(max_heap, -6)

# print(-heapq.heappop(max_heap))

# * approach 2 

# heap = []
# heapq.heappush(heap, (-5, 5))
# heapq.heappush(heap, (-1, 1))
# heapq.heappush(heap, (-8, 8))

# # pop gives largest value
# print(heapq.heappop(heap)[1])
# print(heap)

arr = [10, 4, 15, 7, 2]
max_heap = [-x for x in arr]

heapq.heapify(max_heap)

heapq.heappush(max_heap, -12)

popped = -heapq.heappop(max_heap)
print(popped)
print(max_heap)