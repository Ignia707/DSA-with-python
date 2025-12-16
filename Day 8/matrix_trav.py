test = [
  [10],
  [20],
  [30]
]

def mat_trav(input, direct):
    col_ans = zip(*input)
    if direct == "C":
        return [ele for tup in col_ans for ele in tup]
    
    return [ele for row in input for ele in row]

print(list(mat_trav(test, "C")))