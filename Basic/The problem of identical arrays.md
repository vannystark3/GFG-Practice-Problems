# The problem of identical arrays

### Python
```py
class Solution:
    def isIdentical(self, arr1, arr2):
        d1 = {}
        d2 = {}
        for num in arr1:
            if num not in d1:
                d1[num] = 1
            else:
                d1[num] += 1
        for num in arr2:
            if num not in d2:
                d2[num] = 1
            else:
                d2[num] += 1
        for k in d1:
            if k not in d2:
                return False
            else:
                if d1[k]!=d2[k]:
                    return False
        return True
```
