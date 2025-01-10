# Count distinct elements in every window

### Python
```py
class Solution:
    def countDistinct(self, arr, k):
        brr = []
        l = len(arr)
        for i in range(l-k+1):
            d = set(arr[i:i+k])
            z = len(d)
            brr.append(z)
        return brr
```
