# Value equal to index value

Given an array arr. Your task is to find the elements whose value is equal to that of its index value ( Consider 1-based indexing ).

Note: There can be more than one element in the array which have the same value as its index. You need to include every such element's index. Follows 1-based indexing of the array.

### Examples:
```
Input: arr[] = [15, 2, 45, 4 , 7]
Output: 2 , 4
Explanation: 
Here, arr[2] = 2 exists here.
and arr[4] = 4 exists here.
```
```
Input: arr[] = [1]
Output: 1
Explanation: Here arr[1] = 1 exists.
```
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(k)

Constraints:
 - 1 ≤ arr.size ≤ 10^5
 - 1 ≤ arr[i] ≤ 10^6
   
### Python
```py
class Solution:
    def valueEqualToIndex(self, arr):
        l = len(arr)
        brr = []
        for i in range(l):
            if(i+1 == arr[i]):
                brr.append(i+1)
        
        return brr
```
