
# # * defaultdict

# from collections import defaultdict

# word_count = defaultdict(int)
# words = ["apple", "banana", "apple", "orange", "banana", "apple"]

# print(word_count["ramana"])

# for word in words:
#   word_count[word] += 1

# print(word_count)

# # ! my work

# items = ["apple", "ant", "ball", "bat", "cat"]
# item_group = defaultdict(list)

# print(item_group["a"])

# for item in items:
#   item_group[item[0]].append(item)

# print(item_group)

# # * Counter

# from collections import Counter

# chars = "abracadabra"
# freq = Counter(chars)

# print(freq)
# print(freq.most_common(3))
# print(freq["b"])
# print(list(freq.elements()))

# c1 = Counter("abcde")
# c2 = Counter("cdefg")

# print(f"c1: {c1}")
# print(f"c2: {c2}")
# print(c1 + c2) # ? combine counts
# print(c1 - c2) # ? subtract counts (no negatives)

# # ! my work

# words = ["apple", "banana", "apple", "orange", "banana", "apple"]

# count_words = Counter(words)
# print(count_words.most_common(2))

# pairs = [("fruit", "apple"), ("fruit", "mango"), ("veg", "carrot"), ("veg", "beans")]
# tuple_dict = defaultdict(list)

# for pair in pairs:
#     if  pair[0] == "fruit":
#       tuple_dict["fruit"].append(pair[1])
#     else:
#       tuple_dict["veg"].append(pair[1])

# print(tuple_dict)

# # * more cleaner

# grouped = defaultdict(list)
# for key, value in pairs:
#    grouped[key].append(value)

# print(grouped)

# # * deque

# from collections import deque

# l = [1, 2, 3]

# dq = deque(l)

# dq.append(4)
# print(dq)

# dq.appendleft(0)
# print(dq)

# dq.pop()
# print(dq)

# dq.popleft()
# print(dq)

# ! my work

from collections import deque

dq = deque([1, 4, 5, 7])

dq.append(9)
print(dq)

dq.append(10)
print(dq)

dq.appendleft(90)
print(dq)

dq.pop()
print(dq)

dq.popleft()
print(dq)

