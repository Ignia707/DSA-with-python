
# * defaultdict

from collections import defaultdict

word_count = defaultdict(int)
words = ["apple", "banana", "apple", "orange", "banana", "apple"]

print(word_count["ramana"])

for word in words:
  word_count[word] += 1

print(word_count)

# ! my work

items = ["apple", "ant", "ball", "bat", "cat"]
item_group = defaultdict(list)

print(item_group["a"])

for item in items:
  item_group[item[0]].append(item)

print(item_group)

# * Counter

from collections import Counter

chars = "abracadabra"
freq = Counter(chars)

print(freq)
print(freq.most_common(3))
print(freq["b"])
print(list(freq.elements()))

c1 = Counter("abcde")
c2 = Counter("cdefg")

print(f"c1: {c1}")
print(f"c2: {c2}")
print(c1 + c2) # ? combine counts
print(c1 - c2) # ? subtract counts (no negatives)

# ! my work

words = ["apple", "banana", "apple", "orange", "banana", "apple"]

count_words = Counter(words)
print(count_words.most_common(2))