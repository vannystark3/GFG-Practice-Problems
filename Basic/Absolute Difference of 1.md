# Absolute Difference of 1

### Python
```py
class Solution:
    def getDigitDiff1AndLessK(self, arr, k):
        brr = []
        for num in arr:
            if (num<k and num>=10):
                z = num
                flag = True
                while(num>=10):
                    x = num%10
                    num = num//10
                    y = num%10
                    if (abs(x-y))!=1:
                        flag = False
                if flag:
                    brr.append(z)
                    
        return brr
```
