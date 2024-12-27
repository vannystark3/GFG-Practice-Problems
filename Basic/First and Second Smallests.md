# First and Second Smallests

Given an array, arr of integers, your task is to return the smallest and second smallest element in the array. If the smallest and second smallest do not exist, return -1.

### Examples:
```
Input: arr[] = [2, 4, 3, 5, 6]
Output: 2 3 
Explanation: 2 and 3 are respectively the smallest and second smallest elements in the array.
```
```
Input: arr[] = [1, 1, 1]
Output: -1
Explanation: Only element is 1 which is smallest, so there is no second smallest element.
```


Expected Time Complexity: O(n)
Expected Auxillary Space: O(1)

Constraints:
 - 1 <= arr.size <= 10^5
 - 1 <= arr[i] <= 10^5

### Python
```py
class Solution:
    def minn(self,arr):
        l = len(arr)
        if(l==0):
            return -1
        m = arr[0]
        for num in arr:
            if(num<m):
                m = num
        return m
        
    def minAnd2ndMin(self, arr):
        x = self.minn(arr)
        arr.remove(x)
        y = self.minn(arr)
        while(x==y):
            arr.remove(y)
            y = self.minn(arr)
        if(x==-1 or y==-1):
            return [-1]
        return [x,y]
```
