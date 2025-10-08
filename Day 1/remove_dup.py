nums = [1,1,2,2,3,4,4,5]

def remove_dup_sorted(input):
  return list(set(input))

def remove_dup_inplace(input):
  # denotes the indice in which the next unique element goes
  write_index = 1
  
  for i in range (1, len(input)):
    # scans for unique elements, comparing rear elements
    if (input[i-1] != input[i]):
      # modify the next unique indiced element & increment write_head
      input[write_index] = input[i]
      write_index += 1
  
  return input[:write_index]

print(remove_dup_sorted(nums))
print(remove_dup_inplace(nums))