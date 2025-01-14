# Missing in Array

### Python
```py
class Solution:
    def missingNumber(self, arr):
        l = len(arr)+1
        x1 = (l+1)*(l)//2
        x2 = sum(arr)
        return x1-x2
```
