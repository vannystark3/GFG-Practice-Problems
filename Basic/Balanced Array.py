class Solution:
    def min_value_to_balance(self, arr):
        l = len(arr)
        a = 0
        for i in range(l):
            if(i<l/2):
                a += arr[i]
            else:
                a -= arr[i]
        
        return abs(a)
