# Sum of alternate product

### Python
```py
class Solution:
    def altProduct(self, arr):
        l = len(arr)
        arr.sort()
        s = 0
        for i in range(l//2):
            s += (arr[i]*arr[-(i+1)])
        return s
```
