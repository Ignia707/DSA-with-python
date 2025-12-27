"""
Armsttrong number --> number equal to the sum of it's digits each raised to the total number of digits in the number

I don't think we can do this without iteration / looping regardless

"""

N = 153

def armstrong_base(number):
    summation = 0
    og = number
    length = len(str(number))

    for _ in range(length):
        summation += (number % 10) ** length
        # ! remember "/" gives you float. use "//" to get "int"
        number //= 10

    return og == summation

# print(armstrong_base(N))

def armstrong_improved(N):
    string_n = str(N)
    length = len(string_n)

    return N == sum(int(digit) ** length for digit in string_n)

print(armstrong_improved(N))