# Difference between highest and lowest occurrence

### Python
```py
class Solution:
    def findDiff(self, arr):
        d = {}
        for num in arr:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        a = list(d.values())
        # print(a[0])
        l,s = a[0],a[0]
        for num in a:
            if(num>l):
                l = num
            if(num<s):
                s = num
        return l-s
```
