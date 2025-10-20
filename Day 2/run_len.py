input = "aaabbc"

def run_le (input):
  """
  key takeaways:
  - the count = 1, initially not 0
  - append the i-1th char not ith cuz if the prev & curr ain't same it'll conflict
  - 
  """
  le = 1
  compressed = ""
  for i in range(1, len(input)):
    if input[i-1] == input[i]:
      le += 1
    
    else:
      compressed += f"{input[i-1]}{le}"
      le = 1
  compressed += f"{input[-1]}{le}"

  return compressed
print(run_le(input))

"""
logic:
1. start from 1 index
2. if last and curr not same -> append the char & legth, reset legth
3. if same  -> update legth
"""