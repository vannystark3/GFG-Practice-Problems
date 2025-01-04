# Smaller and Larger

Given a sorted array arr and a value x, return an array of size 2. The first value is the number of elements less than or equal to x, and the second value is the number of elements greater than or equal to x.

### Examples:
```
Input: arr[] = [1, 2, 8, 10, 11, 12, 19],  x = 0
Output: 0, 7
Explanation: There are no elements less or equal to 0 and 7 elements greater to 0.
```
```
Input: arr[] = [1, 5, 8, 12, 12, 12, 19], x = 12
Output: 6, 4
Explanation: There are 6 elements less or equal to 12 and 4 elements greater or equal to 12.
```

Expected Time Complexity: O(logn)
Expected Auxiliary Space: O(1)

Constraints:
 - 1 ≤ arr.size ≤ 10^5
 - 0 ≤ arr[i], x ≤ 10

### Python
```py
class Solution:
    def getMoreAndLess(self, arr, x):
        l = len(arr)
        if(x<arr[0]):
            return [0,l]
        elif(x>arr[-1]):
            return [l,0]
        s,g = 0,0
        for num in arr:
            if num<=x:
                s += 1
            if num>=x:
                g += 1
        return [s,g]
```
