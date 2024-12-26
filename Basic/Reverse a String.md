# Reverse a String

You are given a string s, and your task is to reverse the string.

### Examples:
```
Input: s = "Geeks"
Output: "skeeG"
```
```
Input: s = "for"
Output: "rof"
```
```
Input: s = "a"
Output: "a"
```

Constraints:
 - 1 <= s.size() <= 106
 - s contains only alphabetic characters (both uppercase and lowercase).

### Python
```py
class Solution:
     def reverseString(self, s: str) -> str:
        a = ""
        l = len(s)
        for i in range(l-1,-1,-1):
            a += s[i]
        return a
```
