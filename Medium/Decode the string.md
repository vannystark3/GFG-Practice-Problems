```py
class Solution:
    def decodedString(self, s):
        stack = []
        string = ""
        num = 0
        for char in s:
            if char.isdigit():
                num = num*10 + int(char)
            elif char=='[':
                stack.append((string,num))
                string = ""
                num = 0
            elif char==']':
                prevString,count = stack.pop()
                string = prevString + string*count
            else:
                string += char
        return string
```
