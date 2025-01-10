# Array Duplicates

### Python
```py
class Solution:
    def findDuplicates(self, arr):
        d = {}
        brr = []
        for num in arr:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        for k in d:
            if d[k]>1:
                brr.append(k)
        return brr
```
