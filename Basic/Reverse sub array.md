# Reverse sub array

### Python
```py
class Solution:
	def reverseSubArray(self,arr,l,r):
	    l -= 1
	    r -= 1
		while l<=r:
		    arr[l],arr[r] = arr[r],arr[l]
		    r -= 1
		    l += 1
		return arr
```
