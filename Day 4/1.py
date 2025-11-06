# from collections import Counter

# def topK (nums, k):
#   return [key_map[0] for key_map in Counter(nums).most_common(k)]

# print(topK([1, 1, 1, 2, 2, 3], 2))

from datetime import datetime

now1 = datetime.now()
timestamp_from_datatime = now1.timestamp()
print(timestamp_from_datatime)

import time

timestamp_seconds = time.time()
print(timestamp_seconds)