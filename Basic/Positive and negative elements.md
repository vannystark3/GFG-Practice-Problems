# Positive and negative elements

### Python
```py
class Solution:
    def arranged(self,arr):
        p = 0
        n = 1
        l = len(arr)
        brr = [0]*l
        for i in range(l):
            if arr[i]>0:
                brr[p] = arr[i]
                p += 2
            else:
                brr[n] = arr[i]
                n += 2
        return brr
```
