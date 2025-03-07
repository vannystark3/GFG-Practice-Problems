# Selection Sort

### Python
```py
class Solution: 
    def selectionSort(self, arr):
        l = len(arr)
        for i in range(l):
            mini = l-1
            for j in range(i,l):
                if(arr[j]<arr[mini]):
                    mini = j
            arr[i],arr[mini] = arr[mini],arr[i]
        return arr
```
