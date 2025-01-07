# Minimum Product of k Integers

### Python
```py
class Solution:
    def minProduct(self, arr, k): 
        mod = 10**9 + 7
        arr.sort()
        l = len(arr)
        p = 1
        if(k>l):
            for i in range(l):
                p *= arr[i]
        else:
            for i in range(k):
                p *= arr[i]
        return p%mod
```
