# Maximum product of two numbers

Given an array arr of non-negative integers, return the maximum product of two numbers possible.

### Examples:
```
Input: arr[] = [1, 4, 3, 6, 7, 0] 
Output: 42
Explanation: 6 and 7 have the maximum product.
```
```
Input: arr[] = [1, 100, 42, 4, 23]
Output: 4200
Explanation:  42 and 100 have the maximum product.
```

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
 - 2 ≤ arr.size ≤ 10^7
 - 0 ≤ arr[i] ≤ 10^9

### Python
```py
class Solution:
	def maxProduct(self,arr):
	    arr.sort(reverse=True)
	    return arr[0]*arr[1]
```
