# Third largest element

Given an array, arr of positive integers. Find the third largest element in it. Return -1 if the third largest element is not found.

### Examples:
```
Input: arr[] = [2, 4, 1, 3, 5]
Output: 3
Explanation: The third largest element in the array [2, 4, 1, 3, 5] is 3.
```
```
Input: arr[] = [10, 2]
Output: -1
Explanation: There are less than three elements in the array, so the third largest element cannot be determined.
```
```
Input: arr[] = [5, 5, 5]
Output: 5
Explanation: In the array [5, 5, 5], the third largest element can be considered 5, as there are no other distinct elements.
```

Expected Time Complexity: O(n)
Expected Space Complexity: O(1)

Constraints:
 - 1 ≤ arr.size ≤ 105
 - 1 ≤ arr[i] ≤ 105

### Python
```py
class Solution:
    
    def maxx(self,arr):
        m = arr[0]
        for num in arr:
            if(num>m):
                m = num
        return m
        
    def thirdLargest(self,arr):
        l = len(arr)
        if(l<3):
            return -1
        c = 2
        while(c!=0):
            z = self.maxx(arr)
            arr.remove(z)
            c -= 1
        return self.maxx(arr)
```
