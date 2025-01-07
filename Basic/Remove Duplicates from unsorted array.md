# Remove Duplicates from unsorted array

### Python
```py
class Solution:
    def removeDuplicate(self, arr):
        brr = []
        x = set()
        for num in arr:
            if num not in x:
                x.add(num)
                brr.append(num)
        return brr
```
