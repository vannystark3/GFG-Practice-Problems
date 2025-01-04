# Segregate Even and Odd numbers

Given an array arr, write a program segregating even and odd numbers. The program should put all even numbers first in sorted order, and then odd numbers in sorted order.

Note:- You don't have to return the array, you have to modify it in-place.

### Examples:
```
Input: arr[] = [12, 34, 45, 9, 8, 90, 3]
Output: [8, 12, 34, 90, 3, 9, 45]
Explanation: Even numbers are 12, 34, 8 and 90. Rest are odd numbers.
```
```
Input: arr[] = [0, 1, 2, 3, 4]
Output: [0, 2, 4, 1, 3]
Explanation: 0 2 4 are even and 1 3 are odd numbers.
```
```
Input: arr[] = [10, 22, 4, 6]
Output: [10, 22, 4, 6]
Explanation: Here all elements are even, so no need of segregataion
```

Constraints:
 - 1 ≤ arr.size() ≤ 10^6
 - 0 ≤ arr[i] <=10^5

### Python
```py
class Solution:
	def segregateEvenOdd(self,arr):
	    odd = []
	    even = []
	    for num in arr:
	        if num%2==0:
	            even.append(num)
	        else:
	            odd.append(num)
	    odd.sort()
	    even.sort()
	    brr = even+odd
	    l = len(arr)
	    for i in range(l):
	        arr[i] = brr[i]
```
