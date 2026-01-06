"""

Insertion, Removal -> O(1) average
Worst case -> O(N) 

! If you need sorted keys, use collections.OrderedDict or sorted(dict.keys())

? What to do when collision: Linear Chaining, store them like this: (store actual elements in sorted chains)
! # Conceptual representation ONLY

hash_table = {
    2 : [2],
    5: [5],
    6: [16],
    8: [18, 28, 28, 38, 48], # Chain of collided elements
    9: [139]
}  # ? go to [number % total] index --> count occurences

? only immutable Dtypes as keys
! see doc for best practices 

"""