# Type of array

### Python
```py
class Solution:
    def maxNtype(self,arr):
        m = min(arr)
        n = max(arr)
        i = arr.index(m)
        j = arr.index(n)
        if(m==arr[0] and n==arr[-1]):
            return 1
        elif(m==arr[-1] and n==arr[0]):
            return 2
        elif(i<j):
            return 3
        else:
            return 4
```
