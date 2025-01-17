# Product array puzzle

### Python
```py
class Solution:
        def productExceptSelf(self, arr):
            l = len(arr)
            res = [1]*l
            left = 1
            for i in range(l):
                res[i] *= left
                left *= arr[i]
            right = 1
            for i in range(l-1,-1,-1):
                res[i] *= right
                right *= arr[i]
            
            return res
```
