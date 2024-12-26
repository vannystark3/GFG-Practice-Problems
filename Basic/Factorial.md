# Factorial

Given a positive integer, n. Find the factorial of n.

### Examples:
```
Input: n = 5
Output: 120
Explanation: 5*4*3*2*1 = 120
```
```
Input: n = 4
Output: 24
Explanation: 4*3*2*1 = 24 
```

Constraints:
 - 0 <= n <= 18

### Python
```py
class Solution:
    def factorial (self, n):
        if(n==1):
            return 1
        else:
            return n*self.factorial(n-1)
```
