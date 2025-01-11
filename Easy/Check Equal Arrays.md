# Check Equal Arrays

### Python
```py
class Solution:
    def checkEqual(self,a,b) -> bool:
        a.sort()
        b.sort()
        l1 = len(a)
        for i in range(l1):
            if a[i]!=b[i]:
                return False
        return True
```
