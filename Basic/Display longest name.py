class Solution:
    def longest(self, names):
        i = 0
        l = len(names)
        m = 0
        for j in range(l):
            x = len(names[j])
            if(x>m):
                m = x
                i = j
            elif(x==m):
                continue
        
        return names[i]
