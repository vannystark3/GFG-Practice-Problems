# Find Transition Point
 
### Python
```py
class Solution:
    def transitionPoint(self, arr): 
        l = len(arr)
        for i in range(l):
            if(arr[i]==1):
                return i
        return -1
```
