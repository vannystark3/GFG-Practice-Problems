# Bubble Sort

### Python
```py
class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr):
        l = len(arr)
        for i in range(l):
            for j in range(l-1):
                if(arr[j]>arr[j+1]):
                    arr[j],arr[j+1] = arr[j+1],arr[j]
        return arr
```
