class Solution:
    def printFibb(self,n):
        if(n==0):
            return []
        if(n==1):
            return [1]
    
        arr = [1,1]
        if(n==2):
            return arr
        i = 2
        while(i<n):
            arr.append(arr[i-2]+arr[i-1])
            i += 1
        return arr
