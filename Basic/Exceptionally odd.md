# Exceptionally odd

Given an array of N positive integers where all numbers occur even number of times except one number which occurs odd number of times. Find the exceptional number.

### Examples:
```
Input:
N = 7
Arr[] = {1, 2, 3, 2, 3, 1, 3}
Output: 3
Explaination: 3 occurs three times.
```
```
Input:
N = 7
Arr[] = {5, 7, 2, 7, 5, 2, 5}
Output: 5
Explaination: 5 occurs three times.
```

Your Task:
You don't need to read input or print anything. Your task is to complete the function getOddOccurrence() which takes arr[] and n as input parameters and returns the exceptional number.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
 - 1 ≤ N ≤ 10^5
 - 1 ≤ arr[i] ≤ 10^6

### Python
```py
class Solution:
    def getOddOccurrence(self, arr, n):
        d = {}
        for i in range(n):
            if arr[i] in d:
                d[arr[i]] += 1
            else:
                d[arr[i]] = 1
        for k in d:
            if d[k]%2!=0:
                return k
```
