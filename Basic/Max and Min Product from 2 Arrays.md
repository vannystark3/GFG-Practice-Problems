# Max and Min Product from 2 Arrays

Given two arrays of arr1 and arr2, the task is to calculate the product of the maximum element of the first array arr1, and minimum element of the second array arr2.

### Examples:
```
Input : arr1 = [5, 7, 9, 3, 6, 2],  arr2 = [1, 2, 6, 1, 9]
Output : 9
Explanation: The max in arr1 is 9. The min element in arr2 is 1. The product is 9*1 = 9.
```
```
Input : arr1 = [0, 0, 0, 0],  arr2 = [1, 1, 2]
Output : 0
```

Expected Time Complexity: O(n + m).
Expected Auxiliary Space: O(1).

Constraints:
 - 1 ≤ arr1.size() , arr2.size() ≤ 10^6
 - 0 ≤ arr1i, arr2i ≤ 10^8

### Python
```py
class Solution:
    def find_multiplication(self, arr1, arr2):
        m = arr1[0]
        n = arr2[0]
        for num in arr1:
            if num>m:
                m = num
        for num in arr2:
            if num<n:
                n = num
        return n*m
```
