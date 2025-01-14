# Longest substring with distinct characters

### Python
```py
class Solution:
    def longestUniqueSubstr(self,s):
        a = set()
        lf = 0
        maxl = 0
        l = len(s)
        for ri in range(l):
            while s[ri] in a:
                a.remove(s[lf])
                lf += 1
            a.add(s[ri])
            maxl = max(maxl,ri-lf+1)
        return maxl
```
