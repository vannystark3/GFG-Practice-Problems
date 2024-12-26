# Sorted Array Search

Given an array, arr[] sorted in ascending order and an integer k. Return true if k is present in the array, otherwise, false.

### Examples:
```
Input: arr[] = [1, 2, 3, 4, 6], k = 6
Output: true
Exlpanation: Since, 6 is present in the array at index 4 (0-based indexing), output is true.
```
```
Input: arr[] = [1, 2, 4, 5, 6], k = 3
Output: false
Exlpanation: Since, 3 is not present in the array, output is false.
```
```
Input: arr[] = [2, 3, 5, 6], k = 1
Output: false
```

Constraints:
 - 1 <= arr.size() <= 106
 - 1 <= k <= 106
 - 1 <= arr[i] <= 106

### Python
```py
class Solution:
    def searchInSorted(self,arr, k):
         l = len(arr)
         left,right = 0,l-1
         while (left<=right):
             mid = (left+right)//2
             if(arr[mid]==k):
                 return True
             elif(arr[mid]>k):
                 right = mid-1
             else:
                 left = mid+1
         return False
```
