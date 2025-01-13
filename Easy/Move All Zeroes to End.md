# Move All Zeroes to End

### Python
```py
class Solution:
	def pushZerosToEnd(self,arr):
	    j = 0
	    l = len(arr)
	    for i in range(l):
	        if arr[i]!=0:
	            arr[i],arr[j] = arr[j],arr[i]
	            j += 1
	    return arr
```
