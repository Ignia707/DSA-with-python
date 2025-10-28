input = "aabbbc"
freq_dict = {}
for char in input:
  freq_dict[char] = freq_dict.get(char, 0) + 1 

print(freq_dict)

max_value = max(freq_dict.values())
for key, value in freq_dict.items():
  if value == max_value:
    print(chr(min(ord(max_value), ord(key))))

  elif value > max_value:
    max_value = value
