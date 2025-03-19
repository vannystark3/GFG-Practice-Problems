# Floor in a Sorted Array

### Python
```py
class Solution:
    def findFloor(self,arr,k):
        l = 0
        r = len(arr)-1
        ans = -1
        while l<=r:
            mid = (l+r)//2
            if arr[mid]==k:
                ans = mid
                l += 1
            elif arr[mid]<k:
                l = mid+1
                ans = mid
            else:
                r = mid-1
 
        return ans
```
