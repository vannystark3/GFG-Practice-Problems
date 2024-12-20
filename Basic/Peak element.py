class Solution:   
    def peakElement(self,arr):
        # Code here
        l = len(arr)
        if(l==1):
            return 0
        if(arr[0]>arr[1]):
            return 0
        elif(arr[l-1]>arr[l-2]):
            return l-1
        for i in range(1,l-1):
            if(arr[i]>arr[i+1] and arr[i]>arr[i-1]):
                return i
        return -1
