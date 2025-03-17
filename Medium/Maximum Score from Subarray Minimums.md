# Maximum Score from Subarray Minimums

### Python

```py
class Solution:
    def pairWithMaxSum(self, arr):
        sums = 0
        maxSum = 0
        l = len(arr)
        for i in range(l-1):
            sums = arr[i]+arr[i+1]
            maxSum = max(maxSum,sums)
        return maxSum
```
