class Solution:
    def search(self,arr, x):
        l = len(arr)
        for i in range(l):
            if(arr[i]==x):
                return i
        
        return -1
