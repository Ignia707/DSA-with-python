og_str = "ramana"

def rev_string(s, curr=""):
    if len(s) == 0:
        return curr

    print(curr, s)
    return rev_string(s[:-1], curr + s[-1])

print("output:" + rev_string(og_str))