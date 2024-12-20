class Solution:
    def isLengthEven(self, head):
        if head is None:
            return True
        x = head
        c = 1
        while x.next is not None:
            x = x.next
            c += 1
        if(c%2==0):
            return True
        else:
            return False
