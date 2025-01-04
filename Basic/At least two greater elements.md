# At least two greater elements

Given an array arr of distinct elements, the task is to return an array of all elements except the two greatest elements in sorted order.

### Examples:
```
Input: arr[] = [2, 8, 7, 1, 5]
Output: [1, 2, 5] 
Explanation: Here we return an array contains 1 , 2, 5 and we leave two greatest elements 7 & 8. 
```
```
Input: arr[] = [7, -2, 3, 4, 9, -1]
Output: [-2, -1, 3, 4]
Explanation: Here we return an array contains -2 , -1, 3, 4 and we leave two greatest elements 7 & 9. 
```


Expected Time Complexity: O(nlog(n))
Expected Space Complexity: O(n)

Constraints:
 - 3 ≤ arr.size ≤ 10^5
 - -10^6 ≤ arr[i] ≤ 10^6

### Python
```py
class Solution:
    def findElements(self,arr):
        n = 0
        while n!=2:
            n += 1
            x = max(arr)
            # print(x)
            arr.remove(x)
        arr.sort()
        return arr
```
