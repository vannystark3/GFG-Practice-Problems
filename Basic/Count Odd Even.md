# Count Odd Even

Given an array arr[] of positive integers. The task is to return the count of the number of odd and even elements in the array.

Note: Return an array of two elements where the first one in the count of odd & second one is the count of even.

### Examples:
```
Input: arr[] = [1, 2, 3, 4, 5]
Output: 3 2
Explanation: There are 3 odd elements (1, 3, 5) and 2 even elements (2 and 4).
```
```
Input: arr[] = [1, 1]
Output: 2 0
Explanation: There are 2 odd elements (1, 1) and no even elements.
```

Expected Time Complexity: O(n)
Expected Space Complexity: O(1)

Constraints:
 - 1 <= arr.size <= 10^6
 - 1 <= arr[i] <= 10^6

### Python
```py
class Solution:
	def countOddEven(self, arr):
		l = len(arr)
		c = 0
		for num in arr:
		    if(num%2==0):
		        c += 1
		return [l-c,c]
```
