# Aha Logics:

1. ### chr((ord(char) - 97 + key) % 26 + 97) &rarr; for wrapping ASCII value shift (a-z)

   **LOGIC OF THE SHIFT**

   - [x = ord(char) - 97] -> change to alphabetical index (0 - 25)
   - [y = x + key] -> new alphabetical index
   - "% 26" keeps the value between (0 - 25) <== "%" returns the remainder
   - from the previous step, we got non-overflowing alphabetical index now we add it with "97" to get ASCII value

2.
