class Solution:
    def findTriplet(self, arr):
        arr.sort()
        l = len(arr)
        if(l<3):
            return False
        
        for i in range(l):
            left,right = 0,l-1
            t = arr[i]
            while(left<right):
                sums = arr[left] + arr[right]
                if(sums==t):
                    return True
                if(sums<t):
                    left += 1
                elif(sums>t):
                    right -= 1
                
        return False
