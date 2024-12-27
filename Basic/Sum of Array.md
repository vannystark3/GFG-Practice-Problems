# Sum of Array

You are given an integer array arr[]. The task is to find the sum of it.

### Examples:
```
Input: arr[] = [1, 2, 3, 4]
Output: 10
Explanation: 1 + 2 + 3 + 4 = 10.
```
```
Input: arr[] = [1, 3, 3]
Output: 7
Explanation: 1 + 3 + 3 = 7.
```

Constraints:
 - 1 <= arr.size <= 10^5
 - 1 <= arr[i] <= 10^4

### Python
```py
class Solution:
	def arraySum(self, arr):
	    s = 0
	    for num in arr:
	        s += num
	    return s
```