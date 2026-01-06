input = "AbCdabedfsYIbjnjkFFfcZZZZ"

queries = ['a', 'c', 'z', 'Z', 'F', 'A']

# * brute -> simply iterate over input with query. Then increment if "=="

# * hash array using ord, chr
# * for both upper, lower case alphabets

"""
if lower or upper alone -> use: 
! index = ord(char) - ord('a') 
! index = ord(char) - ord('A') 
"""

def count_char_hash_array(input_str, queries):
    freq = [0] * 256 # ! we're size of ASCII chars to cover all upper and lower

    for char in input_str:
        freq[ord(char)] += 1
    
    for query in queries:
        print(f"Freq of {query}: {freq[ord(query)]}")

count_char_hash_array(input, queries)

