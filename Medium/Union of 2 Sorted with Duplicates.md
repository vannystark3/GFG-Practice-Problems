# Union of 2 Sorted with Duplicates

### Python
```py
class Solution:
    def findUnion(self,a,b):
        i,j = 0,0
        l1,l2 = len(a),len(b)
        res = []
        while i<l1 and j<l2:
            if(a[i]<b[j]):
                if(not res or res[-1]!=a[i]):
                    res.append(a[i])
                i += 1
            elif(a[i]==b[j]):
                if(not res or res[-1]!=a[i]):
                    res.append(a[i])
                i += 1
                j += 1
            elif(b[j]<a[i]):
                if(not res or res[-1]!=b[j]):
                    res.append(b[j])
                j += 1
        
        while i<l1:
            if(not res or a[i]!=res[-1]):
                res.append(a[i])
            i += 1
        while j<l2:
            if(not res or b[j]!=res[-1]):
                res.append(b[j])
            j += 1
            
        return res
```
