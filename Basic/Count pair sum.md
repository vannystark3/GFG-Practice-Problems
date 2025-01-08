# Count pair sum

### Python
```py
class Solution:
    def countPairs(self,arr1, arr2, x):
        d = {}
        c = 0
        for num in arr1:
            a = x-num
            if a not in d:
                d[a] = 1
            else:
                d[a] += 1
        for num in arr2:
            if num in d:
                c += (d[num])
        return c
```
