# Second Largest 

### Python
```py
class Solution:
    def getSecondLargest(self, arr):
        z = max(arr)
        l = len(arr)
        m = 0
        for i in range(0,l):
            if(arr[i]==z):
                continue
            if(arr[i]>m):
                m = arr[i]
        if(m==0):
            return -1
        return m
```
