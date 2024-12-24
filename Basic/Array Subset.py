class Solution:
    def isSubset(self, a, b):
        return set(b).issubset(set(a))
    
    
