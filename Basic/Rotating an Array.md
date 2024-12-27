# Rotating an Array

Given an array arr[]. The task is to rotate the array by d elements where d ≤ arr.size.

### Examples:
```
Input: arr[] = [-1, -2, -3, 4, 5, 6, 7], d = 2
Output: [-3, 4, 5, 6, 7, -1, -2]
Explanation: 
Rotate by 1: [-2, -3, 4, 5, 6, 7, -1]
Rotate by 2: [-3, 4, 5, 6, 7, -1, -2]
```
```
Input: arr[] = [1, 3, 4, 2], d = 3 
Output: [2, 1, 3, 4]
Explanation: After rotating the array three times, the first three elements shift one by one to the right.
```

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
 - 1 ≤ arr.size ≤ 10^6
 - -10^9 ≤ arr[i] ≤ 10^9
 - 0 ≤ d ≤ arr.size

### Python
```py
class Solution:
    def leftRotate(self, arr, d):
        arr[:] = arr[d:] + arr[:d]
```
