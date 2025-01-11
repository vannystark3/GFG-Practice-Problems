# Frequencies in a Limited Array

### Python

```py
class Solution:
    def frequencyCount(self, arr):
        l = len(arr)
        d = {}
        for i in range(1,l+1):
            d[i] = 0
        for num in arr:
            d[num] += 1
        return list(d.values())
```
