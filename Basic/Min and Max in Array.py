class Solution:
    def get_min_max(self, arr):
        a = arr[0]
        b = a
        for num in arr:
            if(a<num):
                a = num
            if(b>num):
                b = num
        return [b,a]
