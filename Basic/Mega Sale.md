# Mega Sale

### Python
```py
class Solution:
    def maxProfit(self, m, arr):
        p = 0
        arr.sort()
        for i in range(0,m):
            if(arr[i]>0):
                break
            p += arr[i]
        return abs(p)
```
