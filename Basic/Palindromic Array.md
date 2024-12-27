# Palindromic Array

Given an array arr[] of positive integers. Return true if all the array elements are palindrome otherwise, return false.

### Examples:
```
Input: arr[] = [111, 222, 333, 444, 555]
Output: true
Explanation:
arr[0] = 111, which is a palindrome number.
arr[1] = 222, which is a palindrome number.
arr[2] = 333, which is a palindrome number.
arr[3] = 444, which is a palindrome number.
arr[4] = 555, which is a palindrome number.
As all numbers are palindrome so This will return true.
```
```
Input: arr[] = [121, 131, 20]
Output: false
Explanation: 20 is not a palindrome hence the output is false.
```

Expected Time Complexity: O(nlogn)
Expected Space Complexity: O(1)

Constraints:
 - 1 <=arr.size<= 20
 - 1 <=arr[i]<= 10^5

### Python
```py
def pallindrome(n):
    a = str(n)
    l = len(a)
    m  = 0
    while(n!=0):
        x = n%10
        m = m*10 + x
        n = n//10
    if(int(a)==m):
        return 1
    else:
        return 0
    
def PalinArray(arr):
    for num in arr:
        if(pallindrome(num)==0):
            return False
    return True
```
