# Linked List Insertion At End

Given the head of a Singly Linked List and a value x, insert that value x at the end of the LinkedList and return the modified Linked List.

### Examples:
```
Input: LinkedList: 1->2->3->4->5 , x = 6
Output: 1->2->3->4->5->6
Explanation: We can see that 6 is inserted at the end of the linkedlist.
```
```
Input: LinkedList: 5->4 , x = 1
Output: 5->4->1
Explanation: We can see that 1 is inserted at the end of the linkedlist.
```

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
 - 0 <= number of nodes <= 10^5
 - 1 <= node->data , x <= 10^3

### Python
```py
class Solution:
    def insertAtEnd(self,head,x):
        h = head
        a = Node(x)
        if head is None:
            return a
        while h.next:
            h = h.next
        h.next = a
        return head
```
