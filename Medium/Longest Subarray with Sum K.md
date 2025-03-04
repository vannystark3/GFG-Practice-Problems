# Longest Subarray with Sum K

### Python
```py
class Solution:
    def longestSubarray(self, arr, k):  
        mapp = {0:-1}
        Sum = 0
        maxi = 0
        for i,num in enumerate(arr):
            Sum += num
            if Sum-k in mapp:
                length = i-mapp[Sum-k]
                maxi = max(maxi,length)
            if Sum not in mapp:
                mapp[Sum] = i
        return maxi
```
