# Binary Array Sorting

You are given a binary array arr[], where each element is either 0 or 1. Your task is to rearrange the array in increasing order in place (without using extra space). You do not need to return anything; simply modify the input array.

### Examples:
```
Input: arr[] = [1, 0, 1, 1, 0]
Output: [0, 0, 1, 1, 1]
Explanation: After arranging the elements in increasing order, elements will be as 0 0 1 1 1.
```
```
Input: arr[] = [1, 0, 1, 1, 1, 1, 1, 0, 0, 0]
Output: [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
Explanation: After arranging the elements in increasing order, elements will be 0 0 0 0 1 1 1 1 1 1.
```
```
Input: arr[] = [1, 1, 1, 1]
Output: [1, 1, 1, 1]
Explanation: Since the array already contains only 1s, no change is needed.
```

Constraints:
 - 1 ≤ arr.size() ≤ 10^6
 - arr[i] ∈ {0,1} for all valid indices i.

### Python
```py
class Solution:
    def binSort(self, arr):
        k = -1
        l = len(arr)
        for i in range(l):
            if(arr[i]==0):
                arr[i],arr[k+1] = arr[k+1],arr[i]
                k += 1
```