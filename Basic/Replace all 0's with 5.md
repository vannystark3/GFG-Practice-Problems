# Replace all 0's with 5

You are given an integer n. You need to convert all zeroes of n to 5.

### Examples:
```
Input: n = 1004
Output: 1554
Explanation: There are two zeroes in 1004 on replacing all zeroes with 5, the new number will be 1554.
```
```
Input: n = 121
Output: 121
Explanation: Since there are no zeroes in 121, the number remains as 121.
```

Expected Time Complexity: O(k)
Expected Auxillary Space: O(1)
Note:  where k is the number of digits in n

Constraints:
 - 1 <= n <= 10^4

### Python
```py
class Solution:
    def convertFive(self, n):
        x = str(n)
        s = ""
        for ch in x:
            if(ch=="0"):
                s += "5"
            else:
                s += ch
        return s
```
