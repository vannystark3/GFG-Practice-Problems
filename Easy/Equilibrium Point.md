# Equilibrium Point

### Python
```py
class Solution:
    def equilibriumPoint(self, arr):
        l = len(arr)
        s = sum(arr)
        x = 0
        for i in range(l):
            y = s-x-arr[i]
            if(x==y):
                return i
            x += arr[i]
        return -1
```
