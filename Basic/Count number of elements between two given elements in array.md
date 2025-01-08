# Count number of elements between two given elements in array

### Python
```py
class Solution:
    def getCount(self, arr, num1, num2):
        l = len(arr)
        for i in range(l):
            if num1==arr[i]:
                a = i
                break
        for i in range(l-1,-1,-1):
            if num2==arr[i]:
                b = i
                break
        if b<=a:
            return 0
        return b-a-1
```
