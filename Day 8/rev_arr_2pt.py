test = arr = []

def reverse_2pt (input):
    if not input:
        return -1

    left, right = 0, len(input) - 1
    while left < right:
        input[left], input[right] = input[right], input[left]
        left += 1
        right-= 1
    return input

print(reverse_2pt(test))