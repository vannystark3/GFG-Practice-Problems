# Missing And Repeating

### Python
```py
class Solution:
    def findTwoElement(self,arr):
        d = {}
        for num in arr:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        l = len(arr)
        for i in range(1,l+1):
            if i not in d:
                a = i
                break
        for k in d:
            if(d[k]==2):
                b = k
                return [b,a]
```
