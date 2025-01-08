# Longest Increasing Subarray

### Python
```py
class Solution:
    def lenOfLongIncSubArr(self, arr):
        c = 1
        l = len(arr)
        m = 0
        if(l==0):
            return 0
        for i in range(0,l-1):
            if(arr[i+1]<=arr[i]):
                c = 1
            else:
                c += 1
            if(c>m):
                    m = c
        return m
```
