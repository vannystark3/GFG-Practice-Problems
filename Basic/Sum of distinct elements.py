class Solution:
	def findSum(self,arr):
	    arr.sort()
	    sums = arr[0]
	    l =  len(arr)
	    for i in range(l-1):
	        if(arr[i]!=arr[i+1]):
	            sums += arr[i+1]
	    return sums
