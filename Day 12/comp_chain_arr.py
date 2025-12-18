arr = [1, 2, 3, 4, 5]

def check_sorted(arr):
    # * combining all() with <= causes it as behaviour of comparison chain
    return all(arr[i] <= arr[i+1] for i in range(len(arr) - 1))

print(check_sorted(arr))