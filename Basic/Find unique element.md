# Find unique element

Given an array of elements occurring in multiples of k, except one element which doesn't occur in multiple of k. Return the unique element.

### Examples:
```
Input: k = 3, arr[] = [6, 2, 5, 2, 2, 6, 6]
Output: 5
Explanation: Every element appears 3 times except 5.
```
```
Input: k = 4, arr[] = [2, 2, 2, 10, 2]
Output: 10
Explanation: Every element appears 4 times except 10.
```

Expected Time Complexity: O(n* log(arr[i]))
Expected Auxiliary Space: O(log(arr[i]))

Constraints:
 - 3<= arr.size()<=2*10^5
 - 2<= k<=2*10^5
 - 1<= arr[i]<=10^9

### Python
```py
class Solution:
    def find_unique(self, k, arr):
        d = {}
        for num in arr:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        for x in d:
            if(d[x]!=k):
                return x
```
