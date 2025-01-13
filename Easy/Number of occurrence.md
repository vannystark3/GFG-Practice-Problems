# Number of occurrence

### Python
```py
class Solution:
    def countFreq(self, arr, target):
        d = {}
        for num in arr:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        if target in d:
            return d[target]
        else:
            return 0
```
