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
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev

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