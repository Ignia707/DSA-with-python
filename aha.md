# Note POINTS:

1. Be very consicous of the input and return types

2. Re-raise errors to log or let python handle it -> reduce redudant code

3. Use built-in methods if possible

4.

# Aha Logics:

1. ### chr((ord(char) - 97 + key) % 26 + 97) &rarr; for wrapping ASCII value shift (a-z)

   **LOGIC OF THE SHIFT**

   - [x = ord(char) - 97] -> change to alphabetical index (0 - 25)
   - [y = x + key] -> new alphabetical index
   - "% 26" keeps the value between (0 - 25) <== "%" returns the remainder
   - from the previous step, we got non-overflowing alphabetical index now we add it with "97" to get ASCII value

2. for least lexicograhpic value char use `min(list_of_chars)`

# Tools

## General ones:

1. .index() -> to get index of char, item from string or list

## Dictionaries:

1. .get()

   - If key exists, it returns its value.
   - If key doesn’t exist, it returns default, but doesn’t add the key to the dict.

2. .items() -> to iterate over keys, values
3. .keys(), .values() -> obvious :)

4. .setdefault()

   - If key exists, it returns its value (does not change it).
   - If key doesn’t exist, it creates the key with default as its value and returns that default.

5. `Concept`:

   - O(1) -> insert, lookup, delete

6. .pop() -> remove key, value then return value of specified key. Can mention `default return`
7. use case -> Fast lookup by key, (Counting, mapping data)

## Sets:

1. .remove() -> removes item but throws error if not found
2. .discard() -> removes item handles error if not found
3. Operations -> (|, &, -)
4. use case -> (Checking existence / removing duplicates), (Mathematical operations (union, intersection))

## Tuples:

1. Iteratable like list
2. Key, value type iteration: (\*values if more than 2 values in the tuple)

   ```
   for key, *values in pairs:
      print(key, values)
   ```

## collections:

1. Counter(iterable)

   - Counter is a dictionary subclass from Python's `collections` module
   - iterable -> list, tuple, string and dictionary
   - designed to count hashable items automatically
   - no need any extra method for checking count and elements between strings, iterables - use this directly
   - .most_commmon(n) -> gets the top n frequent elements
   - .elements() -> Expand back into individual elements (!! Doesn't gurantee order !!)

2. defaultdict(type)

   - automatically creates a default value for missing keys -> more like default value for all keys until and unless changed (no KeyError)
   - `type` -> int, list => int default is "0", list default is "[]"

3. deque
   - implemented as doubly linked list -> slicing / indexing is slower than list
   - Insertion, removal - start, end -> O(n)
   - use when: `need fast FIFO/LIFO` OR `need efficient insertion/deletion from both ends`
