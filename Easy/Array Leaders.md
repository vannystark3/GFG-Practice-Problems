# Array Leaders

### Python

```py
class Solution:
    def leaders(self, arr):
        l = len(arr)
        maxxi = arr[l-1]
        res = [maxxi]
        for i in range(l-2,-1,-1):
            if arr[i]>maxxi:
                maxxi = arr[i]
                res.append(arr[i])
        res = reversed(res)
        return res
```
