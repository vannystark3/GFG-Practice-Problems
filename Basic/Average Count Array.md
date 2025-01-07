# Average Count Array

### Python
```py
class Solution:
    def countArray (self, arr, x) :
        d = {}
        for num in arr:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        
        brr = []
        for num in arr:
            z = (num+x)//2
            if z in d:
                brr.append(d[z])
            else:
                brr.append(0)
        return brr
            
```
