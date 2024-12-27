# Last index of One

Given a string s consisting of only '0's and '1's,  find the last index of the '1' present.

Note: If '1' is not present, return "-1"

### Examples:
```
Input: s = 00001
Output: 4
Explanation: Last index of  1 in given string is 4.
```
```
Input: s = 0
Output: -1
Explanation: Since, 1 is not present, so output is -1.
```

Expected Time Complexity: O(n)
Expected Auxillary Space: O(1)

Constraints:
 - 1 <= |s| <= 10^6
 - s = {0,1}

### Python
```py
class Solution:
    def lastIndex(self, s: str) -> int:
        l = len(s)
        for i in range(l-1,-1,-1):
            if(s[i]=="1"):
                return i
        return -1
```
