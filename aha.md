# Aha Logics:

1. ### chr((ord(char) - 97 + key) % 26 + 97) &rarr; for wrapping ASCII value shift (a-z)

   **LOGIC OF THE SHIFT**

   - [x = ord(char) - 97] -> change to alphabetical index (0 - 25)
   - [y = x + key] -> new alphabetical index
   - "% 26" keeps the value between (0 - 25) <== "%" returns the remainder
   - from the previous step, we got non-overflowing alphabetical index now we add it with "97" to get ASCII value

2. for least lexicograhpic value char use `min(list_of_chars)`

# Tools

## Dictionaries:

1. .get() -> use for getting value & handle missing key scenarios
2. .items() -> to iterate over keys, values
3. .keys(), .values() -> obvious :)
4. .setdefault() -> use for getting key & handle missing key scenarios (.get() but fr keys)
5. `Concept`:

   - O(1) -> insert, lookup, delete

6. .pop() -> remove key, value then return value of specified key. Can mention `default return`
7. use case -> Fast lookup by key, (Counting, mapping data)

## Sets:

1. .remove() -> removes item but throws error if not found
2. .discard() -> removes item handles error if not found
3. Operations -> (|, &, -)
4. use case -> (Checking existence / removing duplicates), (Mathematical operations (union, intersection))
