# Sum of first n terms

Given an integer n, calculate the sum of series 13 + 23 + 33 + 43 + … till n-th term.

### Examples:
```
Input: n = 5
Output: 225
Explanation: 13 + 23 + 33 + 43 + 53 = 225
```
```
Input: n = 7
Output: 784
Explanation: 13 + 23 + 33 + 43 + 53 + 63 + 73 = 784
```
Constraints:
 - 1 <= n <= 200 

### Python
```py
class Solution:
    def cube(self,a):
        return a*a*a
        
    def sumOfSeries(self,n):
        s = 0
        while(n!=0):
            s += self.cube(n)
            n -= 1
        return s
```
