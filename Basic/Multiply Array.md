# Multiply Array

### Python
```py
class Solution:
    def longest(self, arr, n):
        p = 1
        for num in arr:
            p *= num
        return p
```
