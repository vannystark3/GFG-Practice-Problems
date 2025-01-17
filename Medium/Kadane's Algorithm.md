# Kadane's Algorithm

### Python
```py
class Solution:
    def maxSubArraySum(self,arr):
        maxend = arr[0]
        res = arr[0]
        l = len(arr)
        for i in range(1,l):
            maxend = max(maxend+arr[i],arr[i])
            res = max(res,maxend)
        return res
```
