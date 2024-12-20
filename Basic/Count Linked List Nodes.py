class Solution:
    # Function to count nodes of a linked list.
    def getCount(self, head):
        # code here
        if head is None:
            return 0
        x = head
        c = 1
        while x.next is not None:
            x = x.next
            c += 1
        return c
