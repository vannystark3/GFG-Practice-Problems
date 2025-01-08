# Check Arithmetic Progression

### Python
```py
class Solution:
    def checkIsAP(self, arr):
        arr.sort()
        # print(arr)
        d = arr[1]-arr[0]
        # print(d)
        l = len(arr)
        for i in range(1,l-1):
            x = arr[i+1]-arr[i]
            # print(x)
            if x!=d:
                return False
        return True
```
