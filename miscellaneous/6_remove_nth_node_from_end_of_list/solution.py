"""
Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Fast & Slow Pointer Solution
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head
        
        for _ in range(n):
            fast = fast.next
        if fast is None:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        # Remove node
        slow.next = slow.next.next
        
        return head


# Recursive Solution
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def remove(node: Optional[ListNode], n: int):
            # Iterate until None after end of list
            if node is None:
                return 0

            # Iterate to next node
            val = remove(node.next, n)

            if val == n:
                # Remove Node
                t = node.next
                node.next = t.next
            
            return val + 1

        length = remove(head, n)
        if length == n:
            return head.next
        return head