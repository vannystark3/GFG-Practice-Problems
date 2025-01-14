# Container With Most Water

### Python
```py
class Solution:
    def maxWater(self, arr):
        m = 0
        l = len(arr)
        lf = 0
        ri = l-1
        while lf<ri:
            x = min(arr[lf],arr[ri])*(ri-lf)
            if m<x:
                m = x
            if arr[lf]<arr[ri]:
                lf += 1
            else:
                ri -= 1
        return m
```
