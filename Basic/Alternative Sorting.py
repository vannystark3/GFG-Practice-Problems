class Solution:
    def alternateSort(self,arr):
        n = len(arr)
        brr = []
        arr.sort()
        left,right = 0,n-1
        while left<right:
            brr.append(arr[right])
            brr.append(arr[left])
            left += 1
            right -= 1
        if(left==right):
            brr.append(arr[left])
        return brr
