"""

"""

example = "ABCBA"

# * here i used two variables for start and end
def check_palindrome(input, start, end):
    if start == end:
        return True
    
    elif input[start] != input[end]:
        return False

    # ! baka here if you don't put "return" --> the "True" from the final recursion loop will never reach the first recursion loop. So, 
    return check_palindrome(input, start + 1, end - 1)

def check_palindrome_improved(input, ind):
    if ind > (len(input) // 2) - 1: # ! be careful, with ">=" cause ind falls short of 1 per position
        return True

    elif input[ind] != input[len(input) - 1 - ind]:
        return False

    return check_palindrome_improved(input, ind + 1) 

# print(check_palindrome(example, 0, len(example) - 1))
print(check_palindrome_improved(example, 0))