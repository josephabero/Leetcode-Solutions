"""
Reverse Linked List
https://leetcode.com/problems/reverse-linked-list
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Iterative: T - O(n), S - O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Return if empty
        if not head:
            return head

        # Copy first node
        tail = ListNode(head.val, None)

        # Re-route following original nodes to the copied node
        right = head.next
        while right is not None:
            left = right
            right = right.next
            left.next = tail
            tail = left
        
        return tail

# Recursive: T - O(n), S - O(n)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base Case: Null
        if not head:
            return None

        # Maintain Head for Reversed Linked List (Tail)
        new_head = head
        if head.next:
            new_head = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return new_head