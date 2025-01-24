# Print Linked List

### Python

```py
class Solution:
    def printList(self, head):
        if head is None:
            return
        while head:
            print(head.data,end=" ")
            head = head.next
```
