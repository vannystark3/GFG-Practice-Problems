class Solution:
    def check(self, arr1, arr2) -> bool:
        arr1.sort()
        arr2.sort()
        l1 = len(arr1)
        l2 = len(arr2)
        if(l1==l2):
            for i in range(l1):
                if(arr1[i]!=arr2[i]):
                    return False
        else:
            return False
        return True
