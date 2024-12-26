# First Occurence

Find the first occurrence of the string pat in the string txt. The function returns an integer denoting the first occurrence of the string pat in txt (0-based indexing).

Note: You are not allowed to use the inbuilt function. If there is no occurrence then return -1.

### Examples:
```
Input: txt = "GeeksForGeeks", pat = "Fr"
Output: -1
Explanation: Fr is not present in the string GeeksForGeeks as substring.
```
```
Input: txt = "GeeksForGeeks", pat = "For"
Output: 5
Explanation: For is present as substring in GeeksForGeeks from index 5 (0 based indexing).
```
```
Input: txt = "GeeksForGeeks", pat = "gr"
Output: -1
Explanation: gr is not present in the string GeeksForGeeks as substring.
```

Constraints:
 - 1 <= txt.size(),pat.size() <= 1000

### Python
```py
class Solution:
    def firstOccurence(self,txt,pat):
        l = len(pat)
        right = len(txt)-1
        i = 0
        while(i<=right):
            if(txt[i:i+l]==pat):
                return i
            else:
                i += 1
        return -1
```
