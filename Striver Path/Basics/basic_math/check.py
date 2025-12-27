
def isPalindrome(x: int) -> bool:
    og = x
    reversed_x = 0
    flag = False

    if (x < 0):
        flag = True
        x *= -1

    while (x > 0):
        reversed_x = (reversed_x * 10) + (x % 10)
        x //= 10

    if (reversed_x > (2 ** 31) - 1):
        return 0

    return (-reversed_x if flag == True else reversed_x) 

print(isPalindrome(-121))